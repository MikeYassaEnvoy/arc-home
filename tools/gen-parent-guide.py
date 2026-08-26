#!/usr/bin/env python3
"""Generate a fully detailed PARENT-GUIDE.md from content/legs/*.json.
Run from anywhere: python3 tools/gen-parent-guide.py"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

HEADER = """# Parent guide — The Amazing Race: Home Edition

Five legs around the house, playable in one rainy Saturday or spread across
a week of evenings. Full detail for every leg: each step, every challenge
with its checklist, quiz answers (your cheat sheet — he never sees this),
timers, photo prompts and points. Legs unlock in order (finish a leg's pit
stop to unlock the next). Season 2 story: his four rivals from the Québec
trip are BACK for a rematch, and the Rock Hoppers want revenge for the
photo finish.

## The hidden parent menu

Tap the little **version number ("v0.1.0")** in the corner of Race HQ
**7 times**. From there you can:

- **Jump to a leg** (unlocks it and everything before it) — use this if the
  race gets split across days or played out of order.
- **Mark steps complete** — skip anything that doesn't work in your house.
- **Award a badge** manually.
- **Content check** — confirms all the day's content loaded correctly.
- **🏁 Arm the finish line** (long-press) — the finale mat is LOCKED until
  you flip this. Do it quietly before he heads for the driveway.
- **🏆 Replay the finale** — re-runs the whole finish sequence (photo-finish,
  trophy, recap, photo reel) any time. Replay-safe: no duplicate history or
  points. Perfect for grandparents.
- **Full reset** (long-press) — wipes everything. This is how you start a
  brand-new season later.

Kids can also long-press "Skip this stop" on any step — it's honor-system
everywhere; nothing ever requires a photo or a parent password.

## Scoring, badges, rivals (so you can play along)

- Every challenge lists its points; mini-games add up to 10 bonus points per
  session (only the first 8 sessions per leg count, so replaying is harmless).
- Placements are **scripted** — challenge scores never change them. The
  ceremonies explain placements as "time on the course"; points are his
  season score. The arc: 2nd → 4th (the low point) → 1st (comeback!) →
  2nd (heartbreaker) → CHAMPION in a photo finish.
- Badges: one per leg + specials (⭐ First Win, 🇫🇷 French Speaker at the
  Café Français, 📸 Photographer after 10 photos, 🙈 Brave Bite for the
  blindfold taste test — that one is auto-awarded by the challenge).

---
"""

LEGS = {
    0: dict(
        h="Leg 0 — The Rematch Begins (opening ceremony, ~5 minutes)",
        note=None,
        prep="Just hand over the iPad by the front door. Three warm-up "
             "questions, then the ceremony re-introduces all four rival "
             "teams with rematch storylines. Warm-up points don't count "
             "toward the season.",
        mat="**Ceremony — \"Meet the Teams: The Rematch\":** Jon welcomes the "
            "defending champions and re-introduces all four rivals. No "
            "placements. Badge: 🎒 Back in the Race.",
    ),
    1: dict(
        h="Leg 1 — Kitchen Confidential (Front Door → Kitchen)",
        note=None,
        prep="Before the leg, secretly pick **three mystery foods** for the "
             "blindfold taste test — one easy (banana), one trickier (a bit "
             "of cheese), one silly-but-safe (a pickle). Small bites on a "
             "spoon work best. The Brave Bite badge is auto-awarded when he "
             "completes it. For the table-setting roadblock, just point at "
             "the cupboards and let him go.",
        mat="**Mat: 2nd of 5** — Team Maple edges it by forty seconds, "
            "of course. Non-elimination (\"everyone races on!\"). "
            "Badge: 🍳 Kitchen Captain.",
    ),
    2: dict(
        h="Leg 2 — Backyard Expedition (Kitchen → Backyard)",
        note="Rain plan: every challenge works indoors — scavenger out a "
             "window, window count from inside, obstacle laps around the "
             "living room. Nothing needs to be skipped.",
        prep="Zero setup. The scavenger list is deliberately open-ended "
             "(\"something that was not here last week\" accepts any honest "
             "answer). The scripted 4th place lands at this mat — it's his "
             "low point of the season, so play the comeback tease warmly.",
        mat="**Mat: 4th of 5** — the rough night; **Prairie Thunder "
            "eliminated** (they got lost between two rooms of one house). "
            "Badge: 🌿 Backyard Explorer.",
    ),
    3: dict(
        h="Leg 3 — Secrets of the Second Floor (Backyard → Upstairs)",
        note="No second floor? Rename it in your head — any bedroom + "
             "hallway works; the app never checks.",
        prep="Dump **at least 8 matchable sock pairs** in a pile before the "
             "roadblock (mix in a few odd socks for difficulty). The detour "
             "needs either a Lego/blocks bin (Build) or a bookshelf (Books) "
             "— both branches score the same, let him choose. For **Hotel "
             "Room Inspection** you play the white-glove inspector: tour the "
             "room slowly, hum disapprovingly, run one finger along a shelf, "
             "then declare it five stars. The messier the room going in, the "
             "better this one works. This is the comeback leg: first place, "
             "first win of the season.",
        mat="**Mat: 1st — FIRST WIN**, confetti; **The Tide Riders "
            "eliminated** (found asleep in a blanket fort). "
            "Badges: 🧦 Sock Ninja + ⭐ First Win.",
    ),
    4: dict(
        h="Leg 4 — The Couch 500 (Upstairs → Living Room)",
        note="The screen-time leg: two arcade heats bracket real-world "
             "stops, same rhythm as the trip's driving days.",
        prep="You have two cameo roles: snack recipient (Pit Crew Snack "
             "Run) and **French café waiter** — he orders \"Un biscuit, "
             "s'il vous plaît\" and you hand over a cookie with maximum "
             "Parisian dignity. Saying it aloud auto-awards 🇫🇷 French "
             "Speaker. The mat sets up the finale: Maple is finally out, "
             "and it's the Rock Hoppers rematch.",
        mat="**Mat: 2nd of 3** — the Rock Hoppers win the leg; **Team Maple "
            "eliminated** (last for the first time in two seasons). "
            "Badge: 🕹️ Arcade Ace.",
    ),
    5: dict(
        h="Leg 5 — THE FINALE: Race for the House Cup (Living Room → Driveway)",
        note=None,
        prep="**Photo Finish uses the photos he took today** — nudge him to "
             "use the optional camera button during earlier legs so the "
             "final puzzle has material (4+ photos is plenty). Tell him "
             "**press and hold any photo to see it big**. **The finish line "
             "is LOCKED** until you arm it in the parent menu — do the "
             "long-press quietly while he plays Photo Finish, then let him "
             "run out the front door to a real mat/towel on the driveway "
             "before opening the final pit stop. The finale is ~2 minutes "
             "of pure payoff. Don't skip the recap screen; every photo from "
             "the day is in it.",
        mat="**FINISH LINE: photo-finish WIN — BACK-TO-BACK CHAMPIONS!** "
            "Trophy, confetti storm, full season recap. "
            "Badge: 🏆 Race Champion.",
    ),
}

KIND = {
    "drive": "🚗 Drive",
    "detour": "🔀 DETOUR — choose ONE branch",
    "roadblock": "🚧 Roadblock",
    "route-marker": "📍 Route Marker",
    "speed-bump": "⚡ Speed Bump",
    "pit-stop": "🏁 Pit Stop",
}


def fmt_challenge(c, indent="  "):
    out = []
    bits = [c["type"], f"{c['points']} pts"]
    if c.get("timerSeconds"):
        t = c["timerSeconds"]
        bits.append(f"stopwatch target {t//60}:{t%60:02d}" if t >= 60 else f"stopwatch target {t}s")
    out.append(f"{indent}- **{c['title']}** ({' · '.join(bits)}) — {c['instructions']}")
    if c.get("checklist"):
        out.append(f"{indent}  - List: " + " · ".join(c["checklist"]))
    for q in c.get("trivia") or []:
        ans = q["choices"][q["answerIndex"]]
        out.append(f"{indent}  - Q: {q['q']} → **{ans}**")
    if c.get("frenchPhrase"):
        p = c["frenchPhrase"]
        out.append(f"{indent}  - Phrase: *{p['fr']}* (\"{p['phonetic']}\") = {p['en']}")
    if c.get("minigameId"):
        cfg = c.get("config") or {}
        extra = ", ".join(f"{k}: {v}" for k, v in cfg.items())
        out.append(f"{indent}  - Mini-game: `{c['minigameId']}`" + (f" ({extra})" if extra else ""))
    if c.get("photoPrompt"):
        out.append(f"{indent}  - 📸 {c['photoPrompt']}")
    return out


def fmt_step(s):
    out = []
    time = f"{s['scheduledTime']} — " if s.get("scheduledTime") else ""
    out.append(f"**{time}{KIND[s['kind']]}: {s['location']}**")
    if s.get("clueReveal"):
        out.append(f"- Clue says: \"{s['clueReveal']}\"")
    for c in s.get("challenges") or []:
        out.extend(fmt_challenge(c, ""))
    if s.get("detour"):
        for key in ("a", "b"):
            br = s["detour"][key]
            out.append(f"- **Branch {key.upper()} — \"{br['label']}\":** {br['blurb']}")
            for c in br["challenges"]:
                out.extend(fmt_challenge(c, "  "))
    return out


lines = [HEADER]
for leg_id in range(6):
    leg = json.loads((ROOT / f"content/legs/leg-{leg_id}.json").read_text())
    meta = LEGS[leg_id]
    lines.append(f"## {meta['h']}\n")
    if meta["note"]:
        lines.append(f"*({meta['note']})*\n")
    for s in leg["steps"]:
        if s["kind"] == "pit-stop":
            time = f"{s['scheduledTime']} — " if s.get("scheduledTime") else ""
            lines.append(f"**{time}🏁 Pit Stop: {s['location']}**")
            lines.append(f"- {meta['mat']}")
        else:
            lines.extend(fmt_step(s))
        lines.append("")
    lines.append(f"**Prep:** {meta['prep']}\n")

(ROOT / "PARENT-GUIDE.md").write_text("\n".join(lines))
print(f"wrote {len(lines)} lines")
