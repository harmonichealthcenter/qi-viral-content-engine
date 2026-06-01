# PRD: AI Microdrama Content Farm ("Qi Drama Network")

A product requirements document for building a multi-account AI vertical-microdrama operation modeled on the proven farms (909works / aidramalabs network, Premium Episode, AI.Cinema021), repurposed so the David Wong persona and a luxury wellness coil live inside the stories and funnel viewers to the Qi Life brand.

This document is the build spec. All on-screen output it produces must still pass every compliance rule in `content-brain.md` (no medical claims, no banned words, no overt product naming, device as story object only).

---

## 1. How the Real Farms Actually Work

The reference operations are not "a viral channel." They are **factories running a portfolio of accounts** off one pipeline.

- **One operator, many accounts.** 909works runs 6+ TikTok handles (Shape of Desire, Moving into Nightmares, AnimeFlux Daily, etc.) totaling 10M+ followers, all sharing one production line and one collab inbox.
- **Industrialized pipeline.** The Chinese farms compressed the old 11-step live-action process to 3 steps: script to AI parsing to generation. ByteDance Seedance 2.0 and Kuaishou Kling 3.0 render multi-shot sequences with synced audio in ~60 seconds, at a documented usable-footage rate above 90%.
- **Speed and cost.** A series that took 2 months and ~$200K live-action now ships in under 2 weeks for $7K to $14K. ~470 AI dramas are released per day in China.
- **New role created: the AI asset curator.** Translates scripts into prompts and generates locked reference images (characters, costumes, scenes) the video model follows for consistency.
- **Distribution flywheel.** Serialized episodes drop daily. Each new episode pulls back the whole follower base AND gets pushed to new viewers. Cliffhangers force the next tap.

---

## 2. Goal & Success Criteria

**Goal:** Stand up a repeatable, low-cost pipeline that ships serialized AI microdramas across a portfolio of themed accounts, builds a millions-scale audience, and converts attention into Qi Life brand demand without ever making a medical claim.

**Primary success metrics (first 90 days):**
- Ship 3 series (60+ episodes total) across 3 launch accounts.
- Production cost per episode under $15 all-in.
- Production time under 30 min/episode of human touch time after templates are built.
- One account past 100K followers; total network past 250K.
- Measurable funnel signal: RESONANCE comments, profile-link clicks, email captures.

**North-star metric:** Qualified attention captured per dollar of production spend (followers + funnel actions per $).

---

## 3. Business / Monetization Model

Three stacked revenue layers, in priority order for Qi:

1. **Brand funnel (primary).** The drama is top-of-funnel advertising. The device motif and David Wong persona drive curiosity, the CTA captures RESONANCE comments, profile link routes to a landing page / email list / Qi Life store. This is where the real money is for a product company.
2. **Platform creator payouts (secondary).** TikTok Creator Rewards / YouTube Shorts RPM on qualifying long-and-vertical content. Subsidizes production.
3. **Optional licensing / app distribution (later).** Series can be syndicated to microdrama apps (ReelShort/DramaBox-style) or TikTok's PineDrama once the catalog proves out.

The funnel is the point. Platform payouts just make the farm cash-flow neutral while it grows.

---

## 4. System Architecture (The Pipeline)

Five stages, each a swappable module so any single tool can be replaced as models improve.

```
[1 Story Engine] -> [2 Asset Studio] -> [3 Video Gen] -> [4 Assembly] -> [5 Distribution] -> [6 Funnel/Analytics]
```

### Stage 1 — Story Engine (writing)
- Input: a concept from `brain/microdrama-concepts.md`.
- Output: a season bible (characters, world, device rules) + per-episode beat sheet with a cliffhanger every episode and a varied RESONANCE CTA on the closer.
- Tooling: LLM with the Qi content-brain + compliance rules in the system prompt. A compliance lint pass flags any banned word or medical claim before anything is rendered.

### Stage 2 — Asset Studio (consistency layer)
- The AI asset curator builds **character cards**: locked face, wardrobe, posture, and the device prop, generated once per season and referenced in every shot prompt.
- Tooling: Nano Banana / Seedream-class image models for reference stills; a shared prop sheet so the coil looks identical across accounts and series (this is the brand asset).

### Stage 3 — Video Generation
- Per-shot prompts reference the character cards; render 6 to 12 shots per ~75s episode.
- Tooling: Seedance 2.0 / Kling 3.0 (multi-shot + synced audio), Vidu as fallback. Target >90% usable on first pass; reroll failures only.

### Stage 4 — Assembly & Polish
- AI voiceover with emotional mapping (whisper/tension/calm), music, SFX, auto-captions, hook text overlay, episode tag (EP1, EP2...).
- Tooling: ElevenLabs-class voice, an editor (CapCut/Pippit/Morphic-style) for vertical 9:16 cut, burned captions, branded title card.

### Stage 5 — Distribution
- Multi-account scheduler posts daily per account, staggers across time zones, cross-posts winners to YouTube Shorts and Reels.
- Each account profile carries the funnel link and the 909works-style collab email.

### Stage 6 — Funnel & Analytics
- Track per-episode retention, follower delta, RESONANCE comment volume, link clicks, email captures.
- Auto-DM / pinned-comment flow responds to RESONANCE with the next step (landing page).

---

## 5. Recommended Tech Stack

| Layer | Primary | Fallback / Notes |
|---|---|---|
| Scripting + compliance lint | Claude (content-brain prompt) | Any strong LLM; lint is non-negotiable |
| Character / prop reference images | Nano Banana, Seedream | Lock once per season |
| Video generation | Seedance 2.0, Kling 3.0 | Vidu; reroll only failed shots |
| Voiceover | ElevenLabs (emotional) | Keep one consistent David Wong voice ID |
| Editing / captions | CapCut, Pippit, Morphic | Templated title cards + caption style |
| Scheduling / multi-account | Metricool / Postiz / native schedulers | Stagger posting, avoid footprint flags |
| Analytics / funnel | Landing page + email (e.g. ConvertKit) + UTM | Tie RESONANCE to a measurable next step |

---

## 6. Account Portfolio Strategy

Copy the network model, do not bet on one account.

- **Launch 3 themed accounts**, each a different proven engine so the algorithm tells you what wins:
  1. **Cinematic / dystopian** (Shape of Desire lane) — "The Last Calm City" / "The Quiet Neighbor" riff.
  2. **Hidden-wealth / aspirational** (Premium Episode lane) — "The Unbothered Billionaire."
  3. **Absurd / pet** (AI.Cinema021 lane) — "CEO Cat: Office of Calm" for cheap viral reach.
- **Shared spine across all three:** same David Wong voice ID, same glowing-coil prop card, same RESONANCE CTA, same funnel link. Different genre skins.
- **Decouple identities** enough to avoid a single-footprint shadowban (separate emails/devices/IPs as platform rules require), but run them off one pipeline.
- **Double down on winners.** When one account/series breaks out, spin a second account in the same lane and clone the formula.

---

## 7. Content Production Workflow (per episode)

1. Pull next beat from the season bible.
2. Generate script; run compliance lint (banned words, medical claims, product naming). Block on fail.
3. Curator assembles shot prompts against locked character/prop cards.
4. Batch-render shots; reroll only sub-90% shots.
5. Generate VO (David Wong voice), music, SFX.
6. Assemble vertical cut, burn captions + hook overlay + EP tag.
7. QA pass: compliance recheck on final captions/VO, hook strength, cliffhanger present, CTA varied.
8. Schedule; log metadata to analytics.

Human touch time target after templates exist: **under 30 minutes/episode.**

---

## 8. Compliance Layer (NON-NEGOTIABLE for Qi)

Because this farm sells a wellness device, the compliance gate is stricter than a generic drama farm.

- Automated lint blocks the banned word families (treat/cure/heal/diagnose and variants) before render AND on final captions/VO.
- No disease names, no promised outcomes, no medical advice, no on-screen product names.
- The device is **only ever a calm-character story prop**; benefits framed as energy, focus, clarity, sleep, recovery, performance, wellbeing.
- The conversion event is curiosity ("what is that thing on his desk"), resolved off-platform via RESONANCE, not by claims in the video.
- A human compliance reviewer signs off on every season bible before the season renders.

---

## 9. Roadmap

**Phase 0 — Foundations (Week 1-2):** Lock David Wong voice ID + coil prop card. Build script template with embedded compliance lint. Stand up landing page + email capture + UTM funnel.

**Phase 1 — Pilot (Week 3-4):** Produce one 8-episode mini-season on the strongest concept (Unbothered Billionaire or Quiet Neighbor). Manual pipeline end-to-end to find the bottlenecks. Launch 1 account.

**Phase 2 — Templatize (Week 5-8):** Turn the pilot into reusable templates (prompt library, edit template, scheduling cadence). Launch the 3-account portfolio. Hit sub-$15/episode, sub-30-min touch time.

**Phase 3 — Scale (Week 9-12):** Daily posting across all accounts. Double down on the breakout. Add YouTube Shorts + Reels cross-posting. Optimize funnel conversion.

**Phase 4 — Compound (Quarter 2):** Spin sibling accounts on winning lanes. Evaluate microdrama-app / PineDrama syndication. Build a back catalog that keeps converting.

---

## 10. Roles & Team

- **Showrunner / compliance owner** — approves season bibles, owns the brand and the compliance gate.
- **AI asset curator** — character/prop cards, shot prompts, reroll triage. The core operational role.
- **Editor / assembler** — VO, captions, cut, title cards (can be heavily automated).
- **Distribution / growth** — scheduling, multi-account hygiene, funnel and analytics.

A 1-2 person team can run the whole network once Phase 2 templates exist.

---

## 11. Economics (target)

- Per-episode all-in: **under $15** (generation credits + voice + tooling amortized).
- Per 30-episode series: **$300 to $450**, versus $7K-14K studio AI or ~$200K live-action.
- Break-even via platform payouts is plausible at modest scale; the real ROI is funnel-driven Qi sales, measured as attention/funnel-action per dollar.

---

## 12. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Compliance slip (medical claim) | Automated lint + human sign-off; device-as-prop rule; benefits framed in approved language only. |
| Platform AI-content / footprint flags | Disclose AI per platform rules; separate account identities; vary posting; quality over spam. |
| Model quality / consistency drift | Locked character/prop cards; reroll only failed shots; keep one voice ID. |
| Single-account dependency | Portfolio of 3+ accounts; double down on winners only after they prove out. |
| Audience sees through the pitch | Keep device as subtext; let curiosity (not claims) drive RESONANCE. |
| Tool/cost volatility | Modular pipeline; swap any single model as pricing/quality shifts. |

---

## 13. Open Questions

- Funnel destination: Qi Life store directly, or an email list / quiz first?
- Voice: single David Wong voice across all genres, or genre-specific voices sharing the persona?
- AI-disclosure posture per platform as rules tighten in 2026.
- Do we license the back catalog to microdrama apps, or keep it owned-and-operated for funnel control?
