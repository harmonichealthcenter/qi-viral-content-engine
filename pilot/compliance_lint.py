#!/usr/bin/env python3
"""
Compliance lint for the Qi Drama Network pipeline.

This is the hard gate in Stage 1 (Story Engine) and again on final captions/VO
in Stage 4. It blocks any script that contains a banned word, a real product
name, or a likely medical claim BEFORE anything is rendered.

Usage:
    python3 compliance_lint.py path/to/script.txt
    cat script.txt | python3 compliance_lint.py
    python3 compliance_lint.py --json path/to/script.txt

Exit code 0 = clean (safe to render). Exit code 1 = blocked (fix before render).

This is intentionally strict and dependency-free so it can run in any CI step.
It catches obvious violations; it does NOT replace the human compliance
sign-off on every season bible.
"""

import argparse
import json
import re
import sys

# Word families that are never allowed, in any inflection.
# Each entry is matched as a whole word, case-insensitive.
BANNED_WORDS = [
    # treat family
    "treat", "treats", "treating", "treated", "treatment", "treatments",
    # cure family
    "cure", "cures", "curing", "cured",
    # heal family
    "heal", "heals", "healing", "healed",
    # diagnose family
    "diagnose", "diagnoses", "diagnosing", "diagnosed", "diagnosis",
    # substances
    "supplement", "supplements", "pill", "pills", "medicine", "medicines",
    "medication", "medications", "vitamin", "vitamins", "capsule", "capsules",
    "powder", "powders", "nootropic", "nootropics",
]

# Real brand / product names that must never appear on screen.
BANNED_BRANDS = [
    "qi coil", "qi coils", "qicoil", "qi life", "qilife", "qiari",
    "quantum torus",
]

# Phrases that usually signal a medical claim or promised outcome.
# These are softer signals; flagged as violations to force a human rewrite.
CLAIM_PATTERNS = [
    r"\bprevents?\b", r"\breverses?\b", r"\bfixes?\b", r"\brelieves?\b",
    r"\bcures?\b", r"\beliminates?\s+(?:your\s+)?(?:disease|illness|condition|symptom)",
    r"\bclinically proven\b", r"\bmedically proven\b",
    r"\bguarantee[ds]?\b", r"\bdoctor recommended\b",
]

# Em dash is banned by the brand style guide.
EM_DASH = "—"


def find_word_hits(text, words):
    hits = []
    lowered = text.lower()
    for w in words:
        # whole-word, allow internal spaces in multi-word brand names
        pattern = r"(?<!\w)" + re.escape(w) + r"(?!\w)"
        for m in re.finditer(pattern, lowered):
            hits.append((w, m.start()))
    return hits


def find_pattern_hits(text, patterns):
    hits = []
    for p in patterns:
        for m in re.finditer(p, text, flags=re.IGNORECASE):
            hits.append((m.group(0), m.start()))
    return hits


def lint(text):
    violations = []

    for word, pos in find_word_hits(text, BANNED_WORDS):
        violations.append({"type": "banned_word", "match": word, "pos": pos})

    for brand, pos in find_word_hits(text, BANNED_BRANDS):
        violations.append({"type": "banned_brand", "match": brand, "pos": pos})

    for phrase, pos in find_pattern_hits(text, CLAIM_PATTERNS):
        violations.append({"type": "medical_claim", "match": phrase, "pos": pos})

    if EM_DASH in text:
        violations.append({"type": "style", "match": "em dash", "pos": text.index(EM_DASH)})

    # CTA presence check: every episode must invite RESONANCE.
    if "resonance" not in text.lower():
        violations.append({"type": "missing_cta", "match": "RESONANCE", "pos": -1})

    return violations


def context(text, pos, span=30):
    if pos < 0:
        return ""
    start = max(0, pos - span)
    end = min(len(text), pos + span)
    return text[start:end].replace("\n", " ")


def main():
    parser = argparse.ArgumentParser(description="Qi Drama Network compliance lint")
    parser.add_argument("file", nargs="?", help="script file; reads stdin if omitted")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    violations = lint(text)

    if args.json:
        print(json.dumps({"clean": not violations, "violations": violations}, indent=2))
        sys.exit(0 if not violations else 1)

    if not violations:
        print("PASS: clean. Safe to render.")
        sys.exit(0)

    print(f"BLOCKED: {len(violations)} violation(s). Fix before render.\n")
    for v in violations:
        ctx = context(text, v["pos"])
        loc = f"...{ctx}..." if ctx else "(whole script)"
        print(f"  [{v['type']}] '{v['match']}'  {loc}")
    sys.exit(1)


if __name__ == "__main__":
    main()
