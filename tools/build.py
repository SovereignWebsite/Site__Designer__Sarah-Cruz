#!/usr/bin/env python3
"""Build site/index.html and site/designs/1-5.html from tools/template.html.

Edit content in tools/template.html, styles in site/css/, then run:
    python3 tools/build.py
HOME sets which design is the home page.
"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = 1
DESIGNS = [
    (1, "Editorial", "Pastel sections in the colours of Sarah's own portfolio."),
    (2, "Gallery", "The work first: full width images and quiet type."),
    (3, "Label", "Like a fine wine label: cream paper, centred serif and double rules."),
    (4, "Showcase", "Dark gallery walls with copper accents and very large type."),
    (5, "Cut paper", "Torn edges and pasted photographs, after Sarah's collages."),
]
tpl = (ROOT / "tools/template.html").read_text()

def page(n, root, current):
    cards = []
    for i, name, line in DESIGNS:
        href = root + "designs/%d.html" % i
        cur = ' aria-current="page"' if current == i else ""
        cards.append(
            '<a class="card" role="listitem" href="%s"%s>'
            '<img src="%simg/shots/d%d.webp" alt="" width="640" height="400" loading="lazy">'
            '<strong>%d. %s</strong><span>%s</span></a>' % (href, cur, root, i, i, name, line))
    return tpl.replace("{{CARDS}}", "".join(cards)).replace("{{ROOT}}", root).replace("{{N}}", str(n))

(ROOT / "site/designs").mkdir(exist_ok=True)
for n, _, _ in DESIGNS:
    (ROOT / ("site/designs/%d.html" % n)).write_text(page(n, "../", n))
(ROOT / "site/index.html").write_text(page(HOME, "", HOME))
print("built index (design %d) and %d designs" % (HOME, len(DESIGNS)))

items = "".join(
    '<li><a href="%d.html"><strong>%d. %s</strong></a><br>%s</li>' % (i, i, name, line)
    for i, name, line in DESIGNS)
(ROOT / "site/designs/index.html").write_text("""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Choose a design: Sarah Cruz</title><meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="../css/base.css">
<style>main{max-width:40rem;margin:0 auto;padding:3rem 1rem}h1{font-size:2.4rem;margin:0 0 1rem}ol{list-style:none;padding:0}li{padding:1rem 0;border-top:1px solid var(--line)}li a{font-size:1.2rem;display:inline-block;min-height:24px}</style>
</head><body><main id="main"><p class="eyebrow">Sarah Cruz</p><h1>Choose a design</h1>
<p>The same portfolio, five ways. The home page uses design %d.</p><ol>%s</ol>
<p><a href="../">Back to the home page</a></p></main></body></html>
""" % (HOME, items))
print("built designs index")
