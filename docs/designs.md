# Five designs for Sarah's site

Concepts first, code second. Each design is a different way of thinking about Sarah, built from its own section below. All five use only facts already on the site or in public material, and every image is Sarah's own work from her portfolio unless it says otherwise.

Status: built 20 November 2026 as site/designs/1.html to 5.html. The home page uses The Shelf.

## Sources

- Sarah's portfolio PDF (July 2024) and her LinkedIn posts, supplied by Dinis with her permission.
- abundancelondon.com: "a voluntary organisation, founded in 2010, that harvests surplus fruit, plants orchards, hedgerows and trees". It does not name Sarah on the pages read.
- chiswickcheesemarket.uk: "The UK's only specialist cheese market", every third Sunday at The Old Market Place, Chiswick High Road, launched 15 May 2021. Its team page lists Sarah as "Graphic designer". Its media are "All Rights Reserved", so the site links to it and copies nothing.
- Relayed from Dinis through design.b, not yet confirmed by Dinis in this session: Sarah spent a year on the Chiswick Timeline as its main designer, maps and procurement included. Used only once he confirms.

## 1. The Wine List

**Philosophy.** Most of Sarah's work ends up on a wine merchant's list. Show her the way a sommelier would: by region, by producer, with a tasting note.

**Visual narrative.** First: a list header, her name in a large display serif with "Creative Director" as the house line, and a contents column (Retailer exclusives, Independent brands, Spirits, Packaging, Identity, Community). Second: each entry is one line that opens. Project name, client, her one-liner set as a tasting note, disciplines as small notes, awards as a medal mark. Third: opening an entry slides its photographs in beside it.

**Pipeline.** One data file of projects (name, group, client, line, disciplines, award, images). The list is plain HTML `details` elements, so it works with JavaScript off. A small script adds a side panel for the images on wide screens.

**Colour and type.** Ivory list paper, ink black, a claret rule. Large serif for names, small capitals for regions. Light first.

**Unlike the others.** Text leads and images wait to be asked for. It is the fastest way to see everything she has done on one screen.

## 2. The Shelf (dark first)

**Philosophy.** Her packaging is meant to be met on a shelf, under shop light, among rivals. Put it back there.

**Visual narrative.** First: a dark cellar wall and a lit top shelf, with her name on the header board above it. Second: shelves for M&S, Tesco, The Wine Society and Spar, then Independent brands, Spirits and Packaging. Each pack image stands on a shelf edge with a shelf-edge ticket giving the name, her disciplines and any award. Third: choosing a pack brings it forward full screen with its story.

**Pipeline.** The same project data. Each shelf is a row that scrolls sideways and can be reached by keyboard (a labelled region with tabindex). Light falls from above with CSS gradients and shadows. With JavaScript off, the shelves are plain rows of linked images.

**Colour and type.** Near-black wood, warm spotlights, white tickets with a condensed sans. Her photography supplies the colour.

**Unlike the others.** It is the only design that shows her work at the size and in the setting a shopper sees it.

## 3. Front and Back

**Philosophy.** A wine label has a front that sells and a back that tells. The page is one label.

**Visual narrative.** First, the front label: her name as the brand mark; "Brand strategy, identity, packaging, illustration" as the appellation line; "More than 25 years" where a vintage would sit. Second, a turn: the back label is the About, set in small, well-set type, with "Creative Director, Barlow & Co. Formerly Lewis Moberly. West London." as the producer's details. Third: each case study is a label spec card (name, brief in her words, what she did, award).

**Pipeline.** A CSS 3D card that turns between front and back, with prefers-reduced-motion showing both sides flat. Spec cards are a grid built from the project data.

**Colour and type.** Textured cream stock, foil copper for the marks, a fine engraved border. Light first, with a dark "night label" variant.

**Unlike the others.** It treats Sarah herself as the brand, designed the way she would design a label.

## 4. The Timeline (dark first)

**Philosophy.** The Chiswick Timeline is the work she is most proud of: 16 maps of Chiswick from 1592 to today, under a railway bridge, with the river running through every one. Lay her whole story out the same way.

**Visual narrative.** First: dusk under the bridge, the mural strip lit, the blue river line starting at the left edge. Second: travelling along the strip, each panel is a "map" of one group of her work, and the river line carries on through them. Third: the strip arrives at the Timeline itself, with its photographs (the mural, launch day, Sir Peter Blake with his Chiswick Empire, the book) and Abundance London, 2010 to 2020.

**Pipeline.** On wide screens a horizontal strip, scrolled by wheel, keys or drag, inside a labelled region. On phones and with JavaScript off, a vertical strip. The river is one inline SVG path drawn as you go, still under prefers-reduced-motion. Dates are only those already on the page: 1592 to today, 2010 to 2020, the 2022 and 2023 awards.

**Colour and type.** Dusk navy and brick, the river in the mural's blue, map-label type in a fine serif.

**Unlike the others.** It moves sideways, and it puts her community work at the centre rather than at the end.

## 5. Cut Paper

**Philosophy.** Sarah builds a pet portrait in layers of cut and torn paper. Build the page the same way, with the portraits leading.

**Visual narrative.** First: a layered scene with Jack the Australian Shepherd at the centre, pieces of printed paper around him, and her name on a torn strip. The layers drift apart slightly as you scroll. Second: the portraits (Jack, Toby, the cat, and more as she sends them), each on its own sheet with a cut edge and a real shadow. Third: her brand work on overlapping sheets, then a "commission a portrait" sheet.

**Pipeline.** CSS layers with clip-path cut edges and stacked shadows. A small script adds parallax, which is off under prefers-reduced-motion and without JavaScript. There is no text in images.

**Colour and type.** Warm paper, kraft and newsprint greys, one bright accent from the portraits. A hand-cut feel for headings in a system face.

**Unlike the others.** It is for people who come for the portraits, and it is made of the same material as her art.

## The Brief

Not a sixth design but the print stylesheet of all five: her name, roles, the 25+ years line, the clients and awards on the page, and how to get in touch, on two A4 sheets.

## Choosing a design

One "Choose a design" button in the header opens five cards, each with a real screenshot of that design, its name and one line. The current design is outlined. It uses `details` and `summary`, so it needs no script, with plain links as the fallback. The old addresses /designs/1.html to 5.html keep working.
