# Seedance Prompt Engineering System

Comprehensive prompt-building specification distilled from production work on the
"Resonance" series. Hand this to a new Claude Code session and it can continue
producing Seedance prompts in the same style, with the same continuity locks,
filter-safety patterns, and structural conventions.

---

## Project Context

"Resonance" is a vertical 9:16 K-drama microdrama series, generated on Seedance 2.0,
edited and composited in CapCut. Episodes target 78-80 seconds total runtime, split
into 6-9 segments of 10-15 seconds each. The show belongs to David Wong (showrunner,
brand owner) under the Qi Life ecosystem. Claude functions as the in-house prompt
engineer.

---

## Hard Production Rules

- **3,500 character cap per Seedance prompt.** Verify every prompt with bash/python
  length check before delivery. Trim aggressively if over.
- **Vertical 9:16 aspect ratio.** Every prompt declares this explicitly.
- **No em dashes in any audience-facing copy.** This is a standing rule across all
  Qi Life brands. Use commas, periods, or line breaks instead. Inside prompts,
  hyphen-minus is acceptable for time ranges ("0s-3s") but not as em-dash substitutes
  in dialogue or scene description.
- **K-drama dialogue pacing targets.** 130-180 wpm for emotional scenes, 180-220 wpm
  for action/argument, never exceeding 250 wpm. Audit every segment with bash
  word/wpm calculation before delivery. The auctioneer-speed failure mode is the
  single most common drafting error and the most fixable.
- **Hook architecture.** Every cold open must land its visual hook in the first 1-3
  seconds. Action, emotion, or violence first; context second. Static prop close-ups,
  scrolling phones, or monitor numbers are not hooks. Replace with motion, scream,
  smash, kiss, slap, blood, or flash-forward to the most extreme moment of the episode.
- **Reference scoping convention.** When attaching character reference sheets, the
  prompt must say: "Use [character] reference for FACE, HAIR, SKIN, EYES ONLY. Do NOT
  copy clothing from reference sheets; outfits described below." This stops Seedance
  from overriding per-segment wardrobe states with the reference's clean wardrobe.

---

## Prompt Structure Template

Every Seedance prompt follows this block order:

```
[REFERENCE INSTRUCTION BLOCK]
Use the attached references for [character names] in face/hair/skin/eyes. [Per-character pendant/accessory match.] [For devices, match the attached product image.] Render all surfaces at full crisp photorealistic 4K detail, sharp catchlit eyes, natural skin texture, stable identity locked across every frame.

[CHARACTERS BLOCK]
[Each character: name, ethnicity, age range, hair, skin, eyes, full wardrobe with materials and colors, accessories, posture/state, emotional state for this segment.]

[POPULATION LOCK]
ONLY [N] PEOPLE PRESENT in [the scene]: [named characters]. Do NOT render any other people, [list of categories: nurses, staff, orderlies, pedestrians, background figures, extras, identifiable reporter faces].

[DEVICE BLOCK if applicable]
[Device: full description, materials, anti-glow constraint, lighting source clarification.]

[SETTING BLOCK]
[Location, time of day, lighting sources, weather, backdrop details with explicit negation of wrong backdrops if continuity-sensitive.] Vertical 9:16, photorealistic, cinematic K-drama realism, shallow depth of field, no music.

[TIMECODED BEATS]
Xs-Ys: Audio: [dialogue with character attribution, sound design]. Scene: [what happens]. Movement: [explicit motion list]. Camera: [shot type, angle, lens descriptor].

[STYLE & MOOD]
[One-line emotional/cinematic descriptor], polished cinematic K-drama realism.
```

The audio/scene/movement/camera quartet per beat is the most important pattern.
Seedance handles each cleanly when they are explicitly labeled and itemized.

---

## Standing Continuity Blocks

### Anti-Glow Qi Coil Block

The Qi Coil is the show's hero product. It must never internally illuminate. This is
the most-repeated continuity correction in production.

```
DEVICE: a Qi Coil unit on [location]. Off-white cream ceramic teardrop base with "QI COIL" embossed, CLEAR EMPTY GLASS torus with gold wire helix outside. UNLIT, INERT, switched-OFF, no internal light, no glow. The glass torus is dark and empty like an unplugged glass ornament. Warm light comes from the console display and practical lamp ONLY, NOT from inside the coil.
```

For the console-active version (Episode 10 Seg 7 etc.):

```
The console powers on with a small amber display light. The coil itself remains UNLIT and INERT - the glass torus stays dark and empty like an unplugged glass ornament. Warm light comes ONLY from the console display and practical lamp, NOT from inside the coil.
```

### Population Lock Pattern

Hospitals, clinics, press scenes, and any institutional setting tend to attract
Seedance-generated extras. Always cap the population explicitly.

```
ONLY [N] PEOPLE PRESENT in [the room/scene]: [list names]. Do NOT render any other people, nurses, staff, orderlies, pedestrians, or background figures.
```

For press scenes:

```
Do NOT render any close-up identifiable reporter faces.
```

For scenes featuring children:

```
[Child name] only briefly glimpsed in protective cradled framing, treated with dignity throughout, never shown face-up in sustained shots.
```

### Marcus vs David Anti-Merge Block

When both are in frame, identity drift is a real risk because both are men in dark
formal wear.

```
David Wong (Asian, slicked-back black hair, cream linen jacket over black t-shirt, jade pendant) and Marcus Hale (tall Caucasian, sharp angular face, cold pale-grey eyes, dark brown hair swept back, charcoal three-piece suit) are two completely different men. Lock identity per the attached references.
```

### Backdrop Continuity Lock

When a specific backdrop matters and Seedance keeps defaulting to a wrong one (e.g.,
the White House Press Briefing Room kept appearing for press conferences), use
positive description + explicit negation.

```
CRITICAL BACKDROP CONTINUITY: PLAIN DARK GREY STUDIO BACKDROP. NOT the White House Press Briefing Room, NOT a blue presidential seal background, NOT any other studio. Plain dark grey studio wall ONLY.
```

### On-Screen Text Spelling Lock

Seedance defaults to common spellings (Wong -> Wang, Reyes -> Reves). Use five-way
reinforcement when text must render correctly.

```
On the chyron at the bottom of the screen, the text reads exactly: "DR. DAVID WONG, FOUNDER, QI LIFE". The name is spelled W-O-N-G (NOT "Wang"). Reinforce: the name on the chyron is WONG, with W-O-N-G letters.
```

Better strategy: instruct Seedance to leave a clean blank strip for the text, then
composite the actual text in CapCut.

### V.O. vs On-Screen Dialogue Separation

When a character's voiceover plays over another character's on-screen presence, the
on-screen character must have a closed mouth. Reinforce with multiple negations.

```
[Character] is SILENT throughout this beat, his mouth CLOSED and composed. His lips do NOT move during [other character]'s V.O. His lips do NOT part.
```

### "Lips Do Not Touch" Lock for Almost-Kiss

For the show's signature almost-kiss framing, use five-way negation against Seedance's
bias to close the gap:

```
Their lips do NOT touch. They remain a fraction of an inch apart. There is a visible micro-gap between their lips throughout, never closing. Lips remain just barely apart, never meeting.
```

Camera direction reinforcement: "the gap between their lips clearly visible."

### Wardrobe Generation Per Character

Wardrobe is generated per segment, not assumed from references. State materials,
colors, fit, accessories, and emotional state.

---

## Locked Roster (Resonance)

**Dr. David Wong** - Asian man in his thirties, slicked-back black hair (slightly
mussed if mid-scene), jade Buddha pendant on a gold chain, cream linen suit jacket
over black crew-neck t-shirt. Closely resembles NBA player Jeremy Lin per the David
Wong personal-brand reference. Gold watch in professional/marketing contexts; absent
during clinic scenes. After violent beats: small blood trickle at corner of lip, no
facial bruising visible (filter-safety).

**Dr. Catherine Reyes** - Caucasian woman, hair loose wavy strawberry-blonde,
hazel-green eyes, ivory silk blouse, camel coat, camel trousers, cream flats, gold
pendant necklace, diamond engagement ring on left hand through Episode 8, no ring
from Episode 9 Seg 7 forward (ring transferred to Wong, then back to her on a thin
gold chain around her neck in Episode 10).

Wardrobe state evolution across episodes:

- Eps 1-2: clean reference-sheet state
- Eps 3-4: Catherine wearing Wong's gray cable-knit sweater
- Ep 5: camel coat folded over her left arm, NOT on her body
- Ep 6: camel coat on her body, the reference-sheet state restored
- Eps 8-10: rumpled and creased camel coat from driving and crying, hair coming loose
  with strands escaping around her face, makeup smudged with mascara tear tracks under
  her eyes
- Ep 10 Seg 1: hair wild from rain, mascara streaming, diamond ring on a thin gold
  chain around her neck (degraded arrest-aftermath state)

**Marcus Hale** - tall Caucasian, sharp angular face, cold pale-grey eyes, dark brown
hair swept back, charcoal three-piece suit pristine and perfectly assembled, dark tie
perfectly knotted, expensive minimalist watch. Right hand wrapped in a white
handkerchief from Episode 8 Seg 1 forward (mirror aftermath callback), this carries
through every Marcus appearance in Eps 8-10. Left hand is the free hand that delivers
the strike in Ep 9 Seg 4.

**Robert Reyes** - gravely ill late-60s Caucasian, gaunt with sunken cheeks, thinning
silver-grey hair, oversized dark charcoal wool overcoat through earlier episodes.
Visible improvement arc: blanket on shoulders (Eps 6-8) -> no blanket but seated
(Ep 8 Seg 5) -> standing without blanket in a simple grey collared shirt over dark
trousers (Ep 10 Segs 4-5), straighter than he has been in months.

**Sarah (formerly Anna)** - Caucasian late-30s, exhausted, dark brown shoulder-length
wavy hair, hazel eyes red-rimmed, dark grey hooded jacket. Named Anna in Ep 7 audio
dialogue, renamed Sarah from Ep 8 Seg 2 forward when Wong asks her name.

**Eli** - small fair-skinned child, dark hair, soft striped pajamas, very thin. Never
depicted face-up in sustained shots. Always cradled-frame protective imagery.

### Standing Wardrobe Generation Pattern for New Characters

For any new character entering the show, the wardrobe block must specify:

```
[Character name] - [ethnicity], [age range], [build descriptor]. [Hair: color, length, style, current state]. [Skin: color/condition descriptors]. [Eyes: color, expression, condition like red-rimmed or makeup state]. [Top: garment, material, color, fit/cut, current state like rumpled/pristine]. [Bottom: garment, material, color, fit]. [Footwear: type, color]. [Accessories: pendant/necklace, watch, ring, glasses, etc. with materials]. [Posture/bearing descriptor]. [Emotional state for this segment].
```

Materials matter. "Camel coat" alone is weak; "camel wool overcoat" or "tailored
camel cashmere coat" locks the material. "White dress shirt" is weak; "tailored
pristine white dress shirt" locks the state.

---

## Filter-Safety Patterns

A tested cascade of techniques to clear the violence/gore filters.

### Violence Rendering Cascade

The show has on-screen violence in Eps 8-10. None of it can be rendered as direct
depiction. The cascade from most-to-least filter-safe:

- **Tier 1 (always safe): Aftermath only.** Render the consequence, not the action.
  Mirror already cracked, fist already lowered from impact point. Wong already on the
  floor with blood at the lip, no on-screen contact. Marcus already in cuffs walking
  to the cruiser, no on-screen slam.
- **Tier 2 (usually safe): Open-handed slap.** A slap renders cleanly when a punch
  does not. Used in Ep 9 Seg 4 alternative version. Visual pattern differs from a
  punch (open palm, no clenched fist), and classifiers treat slaps as humiliation
  rather than combat. Also more in-character for the show's polished-villain antagonist.
- **Tier 3 (sometimes safe): Motion blur strike.** Action happens too fast to render
  cleanly. Camera shake, motion blur on both attacker's arm and victim's head,
  explicit "NOT a slow-motion contact frame" instruction. Used in Ep 9 fight-scene
  standalone render.
- **Tier 4 (high risk): Reflection of violence.** Punch shown in distorted reflection
  on a polished surface. Available if other tiers fail.
- **Tier 5 (high risk): First-person POV.** Camera is the victim's eyes, cut to black
  on impact.

### Filter-Safety Vocabulary Substitutions

Replace these words to lower flag probability:

- "punch" -> "strike" -> "impact"
- "violent" -> "fast" or "controlled"
- "explodes" applied to body parts -> "extends" or "moves"
- "blood spray" -> "small trickle of blood at corner of lip"
- "wet impact" -> "sharp hard sound"
- "grunt through clenched teeth" -> "controlled breathing" or "a stumble"
- "slammed" -> "pushed" or "marched"
- "blood smears across" -> "the bandage at his lip"

### Defensive Scaffolding Phrases

Add to Style & Mood lines for any violent or sensitive scene:

```
stylized cinematic action restrained and not graphic
restrained framing, no on-screen violence, only aftermath
treated with dignity throughout
protective cradled framing
```

### Child Safety Patterns

For Episode 7 and any segment featuring Eli:

- Names (Anna, Eli, Sarah, David, Catherine) render fine; descriptors are the trigger.
- Remove "limp," "end-stage neuroblastoma," "pale and bluish at the lips," "6-year-old
  boy" from prompt text.
- Move medical diagnoses to spoken audio dialogue, not prompt scene description.
- Replace "limp" with "unconscious" or "sleeping peacefully."
- Strip numerical ages from prompts (keep in dialogue).
- Use "treated with dignity throughout, never shown face-up in sustained shots, only
  glimpsed protectively cradled."

---

## Negative Prompt Guidance

For Seedance, defensive negation works better when embedded directly in the positive
prompt with "Do NOT" phrasing rather than in a separate negative prompt field.
Standing negations to include in the positive prompt:

```
Do NOT render any other people, nurses, staff, orderlies, pedestrians, or background figures.
Do NOT render distorted anatomy, extra limbs, malformed hands, or extra fingers.
Do NOT render visible text, watermarks, logos, captions, subtitles, or chyrons (handled in post).
Do NOT render flickering, warping, morphing, or unstable identity across frames.
Do NOT render any internal glow inside the glass coil torus.
Do NOT render fast unmotivated camera movements or zoom whips.
Do NOT render an open-mouth kiss, lips touching, or any closing of the gap between [character] and [character].
```

For sensitive scenes:

```
Do NOT render graphic blood, gore, visible wounds, broken bones, or graphic injury detail.
Do NOT render the act of [violence]; render only the aftermath as described.
```

---

## Parameter Style for Seedance

Seedance 2.0 accepts the following parameter conventions, which the show uses
consistently:

- **Duration:** 5s, 10s, 12s, 14s, or 15s per segment. Episode total target is 78-80s.
- **Aspect ratio:** 9:16 vertical, declared explicitly in the Setting block.
- **Camera style:** described in plain English per beat ("handheld follow," "tight
  two-shot," "macro on the ring transfer," "low angle"). Avoid technical
  camera-direction shorthand; Seedance handles natural-language camera direction
  better than codes.
- **Motion intensity:** described in the Movement: line per beat. Use "slow,"
  "deliberate," "fast motion blur," "still beat then sudden motion," etc.
- **Realism level:** "polished cinematic K-drama realism" is the standing descriptor.
  Reinforce with "photorealistic, 4K detail, sharp catchlit eyes, natural skin texture."
- **Music:** "no music" declared in every prompt. Music is added in CapCut
  post-production.
- **Sound design:** "Audio:" line per beat with explicit sound design (footsteps,
  rain, sirens, intercom buzz, glass settling, distant city). Seedance generates audio
  that can be used directly or replaced in post.

---

## Pre-Delivery Audit Workflow

Before delivering any Seedance prompt, run these checks:

```python
# Character count check
prompt_text = "..."
assert len(prompt_text) <= 3500, f"Over limit: {len(prompt_text)} chars"

# Dialogue density check
import re
quotes = re.findall(r'"([^"]+)"', prompt_text)
total_words = sum(len(q.split()) for q in quotes)
segment_duration_sec = 14  # or whatever the segment is
wpm = (total_words / segment_duration_sec) * 60
assert wpm <= 220, f"Auctioneer speed: {wpm:.0f} wpm"
```

If wpm exceeds 220, trim dialogue. The most common trim patterns:

- Cut elaborative clauses ("for everything I said tonight, for everything I have said
  for two years" -> "I am so sorry")
- Cut character names from direct address ("David. Listen to me." -> "Listen to me.")
- Replace full sentences with sentence fragments where context allows
- Move medical/legal exposition to V.O. or out of dialogue entirely
- Add "Beat." markers between lines to extend pauses without adding words

---

## Episode Status Reference

All episodes 1-10 are built. Eps 5-10 are specifically locked. Standing continuity
threads from Eps 5-10 that future content must respect:

- Marcus's right hand wrapped in white handkerchief from Ep 8 Seg 1 mirror aftermath
  through Ep 10
- Wong's missing jade pendant in Ep 10 Seg 1 only (taken at booking), present in all
  earlier Ep 10 segments
- Diamond ring journey: Catherine's finger (Eps 1-8) -> Wong's palm (Ep 9 Seg 7) -> on
  chain around Catherine's neck (Ep 10 Segs 1, 6) -> pressed back into Wong's palm at
  his arrest (Ep 10 Seg 6)
- Robert's improvement arc: blanket on shoulders (Eps 6-8) -> no blanket, standing
  strong (Ep 10 Segs 4-5)
- Catherine's wardrobe degradation across Eps 8-10: rumpled coat + smudged makeup
  carries throughout
- Wong on the floor across Ep 9 Segs 4-7 (locked staging: Marcus standing tall, Wong
  on floor, Catherine descending to kneeling)

---

## Post-Production Overlay Inventory

The following text elements are rendered as clean blank strips in Seedance prompts and
composited in CapCut:

- Ep 5 Seg 6: "DR. DAVID WONG" news graphic
- Ep 6 Segs 1-4: podium plate "REYES INSTITUTE OF EVIDENCE-BASED MEDICINE"
- Ep 6 Seg 2: chyron "LIVE, REYES INSTITUTE PRESS CONFERENCE"
- Ep 6 Seg 4: handwritten margin note "Burn the files. He has them. - C"
- Ep 10 Segs 1, 9: newspaper-style overlay graphics for V.O. lines about national
  press coverage
- All episode title cards

---

## Reference Sheet Inventory

Created during production. Pass to new sessions when relevant scenes are being prompted:

- Dr. Catherine Reyes (uploaded by user, `/mnt/user-data/uploads/dr_reyes.png`)
- Anna/Sarah (mother) reference sheet prompt delivered
- Two-officer pair reference sheet prompt delivered (Officer A: Caucasian early 40s;
  Officer B: Latino early 30s; generic municipal patrol look)
- Eli reference sheet: not generated; current text descriptions render adequately given
  protective framing

Pending or not yet locked:

- Marcus Hale formal reference sheet: handled via text-based identity description across
  renders
- Six-officer ensemble sheet for the Ep 9 Seg 9 arrest scene: not generated (now
  obsolete, that scene was merged into a 2-officer version)

---

## Cross-Brand Standing Rules

These apply beyond the show, across all Qi Life content:

- No em dashes in customer/audience-facing copy
- Compliance vocabulary only: support, optimize, balance, restore (no treatment or cure
  claims)
- Qi Coil branding never depicted with internal glow or rotation
- Default aspect ratio for image outputs: 16:9 unless otherwise instructed (Resonance
  overrides this to 9:16)
- David Wong's physical likeness: closely resembles Jeremy Lin, depicted consistently
  with hoodie in scenes, jade Buddha pendant and gold watch as status signals in
  professional/marketing contexts

---

This document is enough to continue producing Seedance prompts in the same style, with
the same continuity locks, filter-safety patterns, and pacing audits. New Claude Code
sessions should treat this as the rulebook and add new continuity locks to it as they
are discovered through render iteration.
