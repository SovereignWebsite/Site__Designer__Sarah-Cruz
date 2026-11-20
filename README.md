# Site__Designer__Sarah-Cruz

Sarah Cruz's design portfolio, live at https://sarah-cruz.designer.sovereignweb.site

- `site/` is the published website: plain HTML, CSS and images, no cookies, no tracking.
- `site/designs/1.html` to `5.html` are five designs of the same facts (The Wine List, The Shelf, Front and Back, The Timeline, Cut Paper). The home page (`site/index.html`) uses design 2. The ideas are in `docs/designs.md`.
- `tools/work.json` holds the projects; `tools/designs.py` holds the other words and builds every page. `site/css/` and `site/js/` hold the looks. Run `python3 tools/designs.py` after editing, and `node tools/shots.js` (with the site served on port 8765) to refresh the chooser screenshots.
- `docs/` has the handover notes for Sarah and her Claude.

Every push to the `dev` branch publishes the site within a minute or two.
