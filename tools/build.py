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
    (1, "Editorial"),
    (2, "Gallery"),
    (3, "Label"),
    (4, "Showcase"),
    (5, "Cut paper"),
]
tpl = (ROOT / "tools/template.html").read_text()

def page(n, root, current):
    links = []
    for i, name in DESIGNS:
        href = (root + "designs/%d.html" % i)
        cur = ' aria-current="page"' if current == i else ""
        links.append('<li><a href="%s"%s>%d. %s</a></li>' % (href, cur, i, name))
    return tpl.replace("{{DESIGNS}}", "".join(links)).replace("{{ROOT}}", root).replace("{{N}}", str(n))

(ROOT / "site/designs").mkdir(exist_ok=True)
for n, _ in DESIGNS:
    (ROOT / ("site/designs/%d.html" % n)).write_text(page(n, "../", n))
(ROOT / "site/index.html").write_text(page(HOME, "", HOME))
print("built index (design %d) and %d designs" % (HOME, len(DESIGNS)))
