# PRD: Qi Viral Content Engine

A closed-loop system that researches the top microdrama channels, mines the
most viral hooks and dramatic patterns, writes compliant scripts in the David
Wong universe, measures how our own published videos perform, and plans the
next video and series from what it learns.

This is the brain that drives the content farm described in
`prd-content-farm.md`. Where that doc specs the production line, this doc specs
the decision loop that tells the line what to make next.

All generated output must pass the compliance gate in `pilot/compliance_lint.py`
and the rules in `brain/content-brain.md` (no medical claims, no banned words,
no on-screen product names, device as story object only).

---

## 1. Problem & Vision

Right now concept and script decisions are manual and intuition-led. The farms
that win (aidramalabs/909works, Premium Episode, AI.Cinema021) win by volume and
fast iteration, not by guessing. We need a system that turns the open signal of
what is already going viral into a continuous, measured pipeline of what we
make next.

**Vision:** A self-improving loop. Every week the engine knows which hooks,
themes, and dramatic beats are working in the market AND on our own channels,
and it plans the next batch accordingly. Humans approve and direct; the engine
does the research, drafting, and measurement.

---

## 2. Goals & Non-Goals

**Goals**
- Continuously catalog top channels, series, and their best-performing videos.
- Extract and rank the viral hooks, themes, and dramatic patterns behind them.
- Generate compliant David Wong scripts that apply those patterns.
- Track performance of our own published videos.
- Close the loop: recommend the next video/series from market + own-channel data.

**Non-Goals**
- Not a video renderer. Rendering/assembly lives in the production farm.
- Not a scraper that violates platform terms. Data comes from compliant sources
  (official APIs, licensed analytics providers, manual/operator input).
- Not a fully autonomous publisher. A human approves every concept and script
  before it enters production.

---

## 3. Users

- **Showrunner / operator** — sets direction, approves concepts and scripts,
  owns compliance sign-off.
- **AI asset curator** — takes approved scripts into the production farm.
- **Growth/analyst** — reviews performance dashboards and the engine's plan.

A 1-2 person team runs the whole loop.

---

## 4. System Overview

Six modules in a continuous loop. Each is independent and swappable.

```
        +-------------------------------------------------------------+
        |                                                             v
[1 Research] -> [2 Hook Miner] -> [3 Pattern Analyzer] -> [4 Script Writer]
        ^                                                             |
        |                                                             v
[6 Planner] <--------------------- [5 Performance Tracker] <--- (published)
```

1. **Research** ingests top channels and series.
2. **Hook Miner** pulls the strongest opening hooks and moments from the best videos.
3. **Pattern Analyzer** finds the repeatable structures, themes, and dramatic beats.
4. **Script Writer** drafts compliant episodes applying those patterns.
5. **Performance Tracker** measures our published videos.
6. **Planner** combines market signal + own-channel results to plan the next video/series, and feeds Research new targets.

---

## 5. Functional Requirements by Module

### Module 1 — Research (market ingestion)
- Maintain a registry of target channels and series (seeded from
  `brain/channel-research-list.md`: aidramalabs network, Premium Episode,
  AI.Cinema021, ReelShort/DramaBox leaderboards, Douyin hits, etc.).
- For each channel, capture: series titles, episode counts, follower counts,
  and per-video view/like/comment/share where the data source exposes it.
- Refresh on a schedule (e.g. weekly) and keep history so trends are visible.
- **Data acquisition (honest constraint):** TikTok/Douyin block automated
  crawling and their pages are not search-indexed at video granularity. So
  Research pulls from, in priority order:
  1. Official platform APIs / research APIs where available.
  2. Licensed third-party analytics providers.
  3. Operator-supplied inputs (screenshots, manual exports, handle lists).
  - The module must record the SOURCE and confidence of every data point and
    never fabricate a view count.

### Module 2 — Hook Miner
- For the top-ranked videos (by views or engagement), capture the first-line
  hook, the cold-open, and the cliffhanger.
- Where transcripts/captions are available, store them; where only operator
  notes exist, store those.
- Tag each hook by type: shock-reveal, betrayal, status-flex, forbidden-desire,
  underdog, mystery, supernatural, etc.
- Rank hooks by the performance of the video they came from.
- Output: a living, ranked **Hook Library** the Script Writer draws from.

### Module 3 — Pattern Analyzer
- Across the catalog, surface recurring patterns:
  - **Theme/engine frequency** (which engines dominate now: anthropomorphic,
    mystic-master, fated-mate, hidden-wealth, mind-reading, revenge, etc.).
  - **Dramatic structure** (hook to escalation to cliffhanger timing, episode
    length, where the biggest view drop-off vs. retention happens).
  - **Dramatic-scene motifs** (the reunion, the reveal, the confrontation, the
    restraint moment) and how often they appear in winners.
- Produce a weekly **Pattern Report**: what is rising, what is saturating, and
  the highest-confidence opportunities.
- Cross-reference market patterns against our own results from Module 5.

### Module 4 — Script Writer
- Input: an approved concept brief from the Planner + relevant entries from the
  Hook Library and Pattern Report.
- Uses `prompts/microdrama-episode-prompt.txt` with the content-brain and the
  David Wong character/coil prop cards.
- Generates: a season bible + per-episode scripts (hook, single story move,
  cliffhanger, varied RESONANCE CTA).
- **Hard gate:** every draft runs through `pilot/compliance_lint.py`. Any
  banned word, brand name, medical-claim pattern, em dash, or missing CTA
  blocks the draft before it reaches a human. Failing drafts are auto-revised
  and re-linted.
- Output goes to the operator for approval, then to the production farm.

### Module 5 — Performance Tracker (our channels)
- Ingest metrics for our own published videos: views, watch-through/retention,
  likes, comments, shares, follower delta, and funnel signals (RESONANCE
  comment volume, profile-link clicks, email captures).
- Attribute each video back to its concept, hook type, theme, and the patterns
  it used, so the system can learn what works for US specifically.
- Detect winners and losers fast (e.g. first-24-hour velocity vs. baseline).
- Feed results into Module 3 (own-channel patterns) and Module 6 (planning).

### Module 6 — Planner (the decision loop)
- Combine: market Pattern Report + our own Performance attribution + catalog
  gaps (engines we have not tried that are winning in market).
- Output a ranked **Content Plan**: the next videos and the next series to make,
  each with a concept brief (engine, hook type, target account/lane, why now).
- Rules of thumb encoded:
  - Double down on our own proven winners (clone the formula, new skin).
  - Enter market-proven engines we are missing (e.g. mystic-master, fated-mate).
  - Retire saturating/declining patterns.
  - Keep a portfolio across the 3 launch lanes (cinematic, hidden-wealth, absurd).
- Briefs flow to Module 4; chosen new targets flow back to Module 1.

---

## 6. Data Model (core entities)

- **Channel**: handle, platform, network, follower history, source/confidence.
- **Series**: title, channel, engine/theme tags, episode count, view history.
- **Video**: series, episode #, hook text, cliffhanger, metrics, source/confidence.
- **Hook**: text, type tags, source video, performance score.
- **Pattern**: description, type (theme/structure/motif), trend direction, evidence.
- **OurVideo**: concept ref, hook type, theme, full funnel metrics.
- **ConceptBrief**: engine, hook type, lane/account, rationale, status.

---

## 7. Tech Stack (proposed)

| Layer | Choice | Notes |
|---|---|---|
| Orchestration | Scheduled jobs / lightweight workflow runner | weekly research + on-publish tracking |
| LLM reasoning | Claude | hook tagging, pattern analysis, script writing, planning |
| Compliance gate | `pilot/compliance_lint.py` | already built and tested |
| Data store | Simple DB (SQLite/Postgres) or structured files in-repo | history + attribution |
| Market data | Official/research APIs + licensed analytics + operator input | never fabricate |
| Own-channel data | Platform creator/analytics APIs | retention + funnel |
| Dashboards | Lightweight reporting (notebook or simple web) | Pattern Report + Plan |

Modular by design so any single source or model can be swapped as the market and
tooling shift.

---

## 8. Compliance Layer (non-negotiable)

- Script Writer cannot emit a draft that fails `compliance_lint.py`.
- Human compliance sign-off on every season bible before production.
- Device stays a story prop; benefits framed only as energy, focus, clarity,
  sleep, recovery, calm, performance, wellbeing.
- No medical claims, no disease names, no promised outcomes, no on-screen brand.
- Research/data modules must respect platform terms and record data provenance.

---

## 9. Metrics & KPIs

**Engine health**
- Research coverage: # channels/series tracked, data freshness.
- Hook Library size and freshness; Pattern Report acted-on rate.

**Output quality**
- Compliance pass rate on first draft (target rising over time).
- Operator approval rate of generated concepts/scripts.

**Business impact (north star)**
- Funnel actions (RESONANCE comments, link clicks, email captures) per video.
- Follower growth per lane; our-channel retention vs. baseline.
- Hit rate: % of planned videos that beat their lane's median view velocity.
- Loop value: improvement in hit rate over time (is the system learning?).

---

## 10. Roadmap

**Phase 1 — Manual loop (Weeks 1-3):** Operator-fed Research (handles +
screenshots), Claude-driven Hook Miner and Pattern Analyzer on that input,
Script Writer + lint already in place. Planner produces a weekly plan by hand
with Claude. Proves the loop end to end with zero infrastructure.

**Phase 2 — Semi-automated (Weeks 4-8):** Add a data store and own-channel
Performance Tracker via platform analytics APIs. Attribution links our results
to hooks/themes. Weekly Pattern Report + Content Plan generated on a schedule.

**Phase 3 — Closed loop (Weeks 9-14):** Automate market data ingestion from
compliant sources, auto-rank hooks, auto-draft + auto-lint scripts for operator
approval, and have the Planner recommend the next batch from combined signal.

**Phase 4 — Compounding (Quarter 2):** The loop tunes itself. Expand to more
lanes/accounts. Back-catalog mined for evergreen winners to re-skin.

---

## 11. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Market data is gated/unscrapable | Compliant sources only; operator input; record provenance; never fabricate. |
| Compliance slip in auto-generated scripts | Hard lint gate + human sign-off; auto-revise loop. |
| Overfitting to market (chasing dead trends) | Planner weights OUR results, retires saturating patterns. |
| Pattern analysis produces generic mush | Tie every pattern to evidence and performance scores, not vibes. |
| Attribution noise (why did a video win?) | Track hook/theme tags per video; look at velocity vs. lane baseline. |
| Single-tool dependency | Modular sources/models; swap without rebuilding the loop. |

---

## 12. Open Questions

- Market data source: which official/licensed providers do we commit to, and
  what is the budget for analytics data?
- Own-channel analytics: which platforms first (TikTok, YouTube Shorts, Reels)?
- How much autonomy does the Planner get before a human must approve a plan?
- Funnel destination and attribution: how do we tie a RESONANCE comment to a
  Qi Life outcome cleanly enough to learn from it?
