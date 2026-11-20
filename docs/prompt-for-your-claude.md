# A prompt for your Claude

## 1. Join the organisation and connect Claude to GitHub

1. Make a GitHub account if you do not have one, and send Dinis your username.
2. Dinis invites you to the SovereignWebsite organisation as a Member and gives you write access to `SovereignWebsite/Site__Designer__Sarah-Cruz`. Both are needed, or Claude's GitHub check fails.
3. Accept at https://github.com/orgs/SovereignWebsite/invitation (the email link may not offer an accept button).
4. On https://claude.ai go to Settings, then Connectors, connect GitHub with the same account, and press "Check again" if it cannot see the repository.
5. Start a new Claude Code session at https://claude.ai/code and pick that repository.

## 2. Paste this message

> I am Sarah Cruz and this repository is my portfolio website, published at https://sarah-cruz.designer.sovereignweb.site. Please read CLAUDE.md, README.md and docs/handover.md first. Projects are in tools/work.json, the other words in tools/designs.py, the looks in site/css/ and site/js/, and you rebuild every page with `python3 tools/designs.py`. Only use facts I give you: never invent a client, a figure or a quote, and credit every photograph. Use plain British English with no em dashes. Keep the site static, with no cookies or tracking. Push to the `dev` branch only; that publishes the site. Show me what you plan to change before you push.
>
> What I would like to change: (write it here)

## 3. Some things you might ask for

- "Use design 3 as my home page."
- "Add these four new pet portraits to the portraits section." (attach the photos)
- "Add my email address to the contact section."
- "Remove the Butternut Box section."
