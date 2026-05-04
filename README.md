# Qi Viral Content Engine

A reusable scriptwriting system for turning raw transcripts into high-energy, viral-ready short-form video scripts for TikTok and YouTube Shorts.

Built around the David Wong persona for the Qi Life / Qi Coil brand. Optimized for HeyGen production.

---

## What This System Does

You give it a transcript (an interview, a podcast clip, a voice memo, your own ramble, anything).

It gives you back a clean, plain-text script that is:
- Hook-driven (designed to stop the scroll)
- Curiosity-loaded (people watch to find out)
- Short, punchy, fast-paced
- Compliant (no medical claims, no banned words)
- Ready to drop straight into HeyGen

No formatting, no bullet points, no labels, no em dashes. Just clean speakable text.

---

## What's In This Repo

```
qi-viral-content-engine/
├── README.md              ← you are here
├── CLAUDE.md              ← rules Claude must follow inside this project
├── prompts/
│   ├── main-script-prompt.txt    ← paste this to generate ONE script
│   └── batch-script-prompt.txt   ← paste this to generate 5-10 scripts
├── brain/
│   └── content-brain.md          ← brand, persona, tone, compliance
├── examples/
│   ├── input-example.txt         ← sample transcript
│   └── output-example.txt        ← sample finished script
└── scripts/
    └── generate-script.md        ← 3-step instructions
```

---

## How To Use It In Claude (Beginner Walkthrough)

### Option A: Use it inside a Claude Project (recommended)

1. Go to claude.ai and click **Projects** in the sidebar.
2. Click **New project** and name it `Qi Viral Content Engine`.
3. Click **Add content** or **Project knowledge** and upload these files:
   - `CLAUDE.md`
   - `brain/content-brain.md`
   - `prompts/main-script-prompt.txt`
   - `examples/input-example.txt`
   - `examples/output-example.txt`
4. In the project's custom instructions box, paste the contents of `CLAUDE.md`.
5. Open a new chat inside that project. You're ready.

### Option B: Use it in any normal Claude chat (no project setup)

1. Open a new chat at claude.ai.
2. Open `prompts/main-script-prompt.txt` and copy everything inside.
3. Paste it into the chat as your first message.
4. Hit send. Claude will respond saying it's ready.
5. Paste your transcript as your next message.
6. Claude returns the finished script.

---

## How To Generate A Single Script (3 Steps)

1. Copy the contents of `prompts/main-script-prompt.txt`.
2. Paste it into Claude.
3. Paste your transcript. Hit send.

Claude returns one clean script in plain text.

---

## How To Generate Multiple Scripts At Once (Batch Mode)

1. Copy the contents of `prompts/batch-script-prompt.txt`.
2. Paste it into Claude.
3. Paste one transcript or several transcripts separated by `---`.
4. Tell Claude how many scripts you want (5 to 10).

Claude returns that many scripts, each one separated clearly.

---

## Output Rules (What You'll Always Get)

Every script follows the same shape:

- A shocking, curiosity-driven hook in the first sentence
- A short science-aware body
- The word `RESONANCE` as the call to action at the end
- Plain text only
- No em dashes
- No bullet points, headings, labels, or JSON
- Casual but intelligent tone
- 1 to 2 minutes when spoken at normal pace

If something comes back with formatting, em dashes, or banned words, just tell Claude "follow the output rules in CLAUDE.md" and it'll fix it.

---

## Banned Words (Never In Output)

- treat
- cure
- heal
- diagnose

Plus no disease names, no medical claims, no specific health outcome promises, no product pitching inside the script.

---

## Tips For Better Scripts

- Feed in a transcript with at least one interesting fact, study, or counterintuitive idea.
- The juicier the source material, the juicier the script.
- If a script feels flat, ask Claude: "make the hook more shocking" or "tighten the body, cut 30%."
- For batch mode, mix transcript topics. You'll get a more varied content slate.

---

## What This System Is NOT For

- Long-form video scripts (over 2 minutes)
- Product sales scripts or ads
- Anything with medical advice or treatment claims
- Written articles or blog posts (use a different prompt)

---

## Future Automation

This repo is structured so you can plug it into n8n, HeyGen, or a Claude Code workflow later. The prompts live in flat text files on purpose. Any automation tool can read them, swap the transcript, and post the result.

---

Built for the Qi Life ecosystem.
