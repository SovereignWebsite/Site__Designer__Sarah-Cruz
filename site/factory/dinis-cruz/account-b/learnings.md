# Learnings

- Commits must be signed with my own key. The platform sets `gpg.ssh.program` to its own signer, so set it locally to `ssh-keygen` before the first commit.
- The ssh-agent holding the signing key can die between turns. Check with `ssh-add -l` and restart it before committing.
- Images pasted inline in a chat do not reach disk. Ask for files.
- Never name private people (mentors, collaborators) without their consent, even in internal docs.
- Facts relayed through other agents are not confirmed until Dinis or Sarah says so. Still open: the Chiswick Timeline year as main designer, the Cheese Market role beyond "Graphic designer", the cow animations, contact email, current role.
- Org-wide policy applies may skip this repository; check that site/policy/ is present after one.
- Scrolling regions need tabindex and a label; test at 320px for sideways scroll.
