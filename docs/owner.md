# For the owner: what you can do on this site yourself

Site: https://sarah-cruz.designer.sovereignweb.site
Repository: https://github.com/SovereignWebsite/Site__Designer__Sarah-Cruz (branch `dev`; every push to `dev` publishes)

Nothing here waits on anyone. Do any of these yourself, in any order, with your own Claude (paste the prompt from `docs/prompt-for-your-claude.md` or https://sarah-cruz.designer.sovereignweb.site/start/).

## Hand the site to Sarah

1. Ask Sarah for her GitHub username.
2. Invite her to the SovereignWebsite organisation as a Member (no teams): https://github.com/orgs/SovereignWebsite/people
3. Give her write access to this repository: https://github.com/SovereignWebsite/Site__Designer__Sarah-Cruz/settings/access
4. Send her https://sarah-cruz.designer.sovereignweb.site/start/ and `docs/questions-for-sarah.md`.

## Add or correct facts

Facts are in `tools/work.json` (projects) and at the top of `tools/designs.py` (about, the Timeline, portraits, contact). Run `python3 tools/designs.py` after editing. Open items, each yours to settle:

- The Chiswick Timeline: relayed but not yet on the site, that Sarah spent a year on it as main designer, maps and procurement included. If true, add it to `TL_TEXT` in `tools/designs.py`, citing yourself.
- Chiswick Cheese Market: the site says "Graphic designer" (from the market's own team page). If she is also behind the market or makes its cow animations, change `FACTS` and add a line; link to the market, do not copy its media (they are "All Rights Reserved").
- Contact: only LinkedIn and cruzandcruz.co.uk are shown. Add an email in `CONTACT` if Sarah wants one.
- Her current role: whether she is looking for a Creative Director role.
- People: Sarah's mentors and Abundance London co-founder are not named, by choice, until they agree.

## Add photos

Put images in `site/img/` and add them:
- a new cut paper portrait: add a line to `PORTRAITS` in `tools/designs.py` (file name, alt text, width, height, caption);
- a new project: add an entry to the right group in `tools/work.json`.
Waiting to be added when you have the files: the Irish setter (finished and two in progress), the terrier, and the Maid of Bruton post images.

## Choose the home design

Five designs are at https://sarah-cruz.designer.sovereignweb.site/designs/. Set `HOME` in `tools/designs.py` to 1 to 5 (now 2, The Shelf).

## Checks and rules

Every push runs the checks (links, previews, no dashes, leak scan, HTML validity, accessibility). If one fails, nothing is published and the run says why. The rules are in `CLAUDE.md` and the Agent Behaviour Policy at https://sarah-cruz.designer.sovereignweb.site/policy/. As owner you do not need to sign commits.
