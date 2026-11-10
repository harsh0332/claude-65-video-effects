---
name: effects
description: Add any of 65 video effects to a talking-head video (orbit, spotlight, glass widgets, timeline, checklist, comment box, phone fan, liquid glass graph, match-cut, live cursor, clone row, day dial, orbit ring, code body, post wall, letter dive, layer explode, sketch words, blade slice, banknote, voice note, impact frame, dolly zoom, newspaper front page, paper tear, blow away and more). Effects track the speaker's face and can sit behind their head. Use when the user types /effects, names one of the effects, or asks to add an effect, zoom, grade, sticker or animation to their video.
---

# Effects: 65 video effects for talking-head videos

The user is usually not technical. Keep replies short and friendly, do the work for them, and never ask them to run commands themselves.

All paths below are relative to this skill's folder (the folder this SKILL.md is in). Use its absolute path in commands.

## 1. First run: set up (once)
Run `bash scripts/setup.sh`. It prints `READY` when done (the first time takes 1 to 3 minutes).
- `NEED_FFMPEG`: install it for them. On a Mac: `brew install ffmpeg` (if `brew` is missing, tell them to install Homebrew from brew.sh first). On Windows: `winget install ffmpeg`.
- `NEED_PYTHON`: install Python 3.12 (Mac: `brew install python@3.12`, Windows: `winget install Python.Python.3.12`), then run setup again.
- On Windows, the Python is at `.venv\Scripts\python.exe` instead of `.venv/bin/python`.

## 2. Get the video and the effect
- Video: the user drags the file into the chat, or gives a path. A vertical phone video works best.
- Effect: from `/effects <name>`, or from what they describe. Match their words to the table below. Unsure? Show them the list.

## 3. Find the timing
- If they say "on the word X" or "when I say ...", run `.venv/bin/python scripts/words.py <video>` and use those times.
- If they give no timing, apply the effect for the whole clip, or ask which part (one short question).
- Short windows look best: 1.5 to 4 seconds per effect.

## 4. Draft, check, render
1. Write the plan next to their video as `<video-name>_effects.json`:
   ```json
   {"effects": [
     {"fx": "orbit", "start": 3.2, "end": 6.0},
     {"fx": "backdrop-word", "start": 14.0, "end": 16.3, "text": "CLAUDE"}
   ]}
   ```
2. Check frames first (fast): `.venv/bin/python scripts/fx.py --plan <plan.json> <video> <folder>/check.png --still 4.5,15.2`, using the middle of each effect. Look at the PNGs yourself. Fix the text, timing or options if something looks off (covers the face, cut off by the edge, unreadable).
3. Render: `.venv/bin/python scripts/fx.py --plan <plan.json> <video> <video-name>_effects.mp4`. The output keeps their original audio. It renders at 1080p by default; add `--width 2160` for 4K (slower).
4. Tell them where the file is. Remind them in one line to watch it before posting: it drafts, they approve.

A single effect needs no plan: `.venv/bin/python scripts/fx.py orbit <video> <out.mp4> --start 3 --end 6 --text "..." --opt key=value`.

## The 65 effects
| # | `fx` name | What it does | Options (all optional) |
|---|---|---|---|
| 1 | `noise` | Reels pile up behind your head, one every quarter second | `images` (folder of screenshots or clips), `size` |
| 2 | `lineup` | Numbered tiles fan out in an arc above your head | `text` (tile names joined with `\|`) |
| 3 | `locked-on` | Corner brackets snap onto your face, the camera follows you | `zoom` (default 1.35), `text` (tag) |
| 4 | `orbit` | Your reels circle your head: in front at the bottom, behind at the top | `images`, `count`, `speed`, `size` |
| 5 | `lean-in` | A fast punch-in on one word | `zoom` (default 1.45, max 2), `speed` |
| 6 | `backdrop-word` | A giant word drops in behind you | `text`, `color` (hex), `font` (`bold` or `serif`) |
| 7 | `spotlight` | Kills the lights, keeps you lit | `text` (glowing word behind you), `color`, `push` |
| 8 | `the-bill` | Prints your instructions like a receipt into the wall above your head | `text` (lines joined with `\|`) |
| 9 | `moody` | A moody colour grade | `grade` (`moody`, `bw`, `warm`, `cool`, `pop`) |
| 10 | `swipe` | A before and after slider sweeps across you | `grade` (the "after" look) |
| 11 | `todo` | A checklist card beside your head ticks off as you talk | `text` (items with `\|`), `ticks` (video seconds with `\|`), `title` |
| 12 | `comment-box` | An Instagram comment bar types a word and posts it | `text` (default EFFECTS) |
| 13 | `tap` | A Follow button pops up and flips to Following | `at` (video second of the flip), `x`, `y` (0 to 1), `color` |
| 14 | `pause-point` | Freezes the frame and points at you with a hand-drawn arrow | `text` (label), `color`, `label_x` |
| 15 | `uninstall` | A glitchy uninstall bar breaks the frame apart | `text` |
| 16 | `reel-frame` | Your video shrinks into an Instagram reel card | `text` (handle) |
| 17 | `shortcut-rain` | Keyboard keys rain down behind you | `text` (keys with `\|`), `count` |
| 18 | `reject-stamp` | A big red stamp slams onto the screen | `text`, `color`, `angle`, `y` |
| 19 | `countdown-flip` | A 3, 2, 1 flip clock above your head | `from` |
| 20 | `rabbit-hole` | The frame tunnels into itself, spinning | `ratio`, `speed`, `spin` |
| 21 | `cover-star` | You become a magazine cover, title behind your head | `text` (title), `lines` (with `\|`), `issue`, `color` |
| 22 | `scribble` | Marker doodles draw themselves around you | `text` (label), `color` |
| 23 | `glass-widgets` | Frosted glass widgets and mini artifacts float around your head, plus an Edited by Claude pill | `text` (big number), `name`, `handle`, `look` (`simple` for the 3-widget version) |
| 24 | `red-collage` | Black and white you, a giant red word behind, three lines slam in | `text` (red word), `lines` (with `\|`), `tag` |
| 25 | `split-headline` | A headline card slides down and pushes you to the bottom half | `text` (lines with `\|`), `hl` (highlighted word), `pill` |
| 26 | `pastel-word` | Lavender room, giant word behind you, a profile card gets followed | `text`, `name`, `handle` |
| 27 | `check-pills` | Grid-paper room, reel boards behind you, a cursor clicks blue pills | `text` (pills with `\|`), `images` |
| 28 | `timeline` | A dark red film grade with an editing timeline, a REC timecode and a glowing playhead | `text` (title), `sub`, `tc` |
| 29 | `headline-box` | A punch-in with a two-line headline, the second line in a white box | `text` (lines with `\|`), `zoom` |
| 30 | `profile-wall` | Your reels grid fills the wall behind you while a counter ticks up | `images`, `count`, `label` |
| 31 | `tier-list` | A tier list drops in and Claude flies into S tier | `title`, `item`, `others` |
| 32 | `broll-split` | B-roll on top with a price-tag sticker, you below | `images`, `text` (tag) |
| 33 | `phone-fan` | Your reels fan out like a hand of phones under a headline | `images`, `text` (lines with `\|`) |
| 34 | `dot-reveal` | Your shot builds out of glowing dots, then snaps to the full picture | `color`, `cell` |
| 35 | `headline-wall` | Your own headlines pile up behind your head, then a total pops in front | `text` (`headline::meta\|...`), `total`, `label` |
| 36 | `checklist` | A Claude task list under your chin: each step spins, then ticks green | `text` (`step::meta\|...`), `title` |
| 37 | `liquid-glass-graph` | A liquid glass card under your chin: a green graph climbs while the number counts up | `text` (label), `from`, `to` (e.g. `197K`, `59%`), `color` |
| 38 | `carousel-spin` | Your reels spin around you in a 3D carousel, then slow to a stop | `images`, `count`, `size`, `turns` |
| 39 | `match-cut` | News pages cut on one word, locked in a red box behind your head | `text` (the word, default Claude), `color` |
| 40 | `apple-toggles` | An iPhone settings card under your chin flips its switches on, one line at a time | `text` (rows with `\|`), `ticks` (seconds with `\|`), `color` |
| 41 | `led-sign` | The lights drop and a glowing LED sign types itself out behind you | `text` (lines with `\|`), `color`, `push` |
| 42 | `slow-push` | A slow cinematic push-in to your face while the room melts out of focus | `zoom` (default 1.6), `blur` |
| 43 | `over-the-shoulder-zoom` | The camera pushes into one top corner and a see-through liquid glass graph pops beside your head (line climbs, number counts up), pulls back, then the other corner with a second, related bar graph. Your head stays in front | `text` (two labels with `\|`), `to` (two numbers with `\|`, e.g. `197K\|672K`), `zoom` (default 2.0) |
| 44 | `messages` | iMessage notifications pop in one after another, creamy glass with a soft glow, stacking up above the bottom of the frame | `text` (messages with `\|`), `title` (default Messages), `y` |
| 45 | `place-in-grid` | You shrink into the centre tile of your 3x3 profile grid on frosted glass, then 8 reels pop in around you, one per frame, with Instagram view counts on every tile | `images` (folder of your reels or covers), `views` (9 counts with `\|`, the 9th is yours) |
| 46 | `live-cursor` | A cursor named Claude selects you with a box, then drags you left and right like a layer | `text` (cursor name), `color`, `drag` (0.07; 0 = off), `plate` |
| 47 | `clone-row` | Copies of you line up behind both shoulders | `count` (3) |
| 48 | `day-dial` | The wall wipes into cream paper with a big clock dial behind your head | `text` (word on the dial), `size` |
| 49 | `predict-keys` | A phone keyboard slides up and types your words with the suggestion bar | `text`, `next` |
| 50 | `orbit-ring` | Your words circle your head as a tilted ring, passing behind you | `text`, `color`, `size`, `speed`, `tilt` |
| 51 | `code-body` | You become running code: coloured body, cream skin, dark room | `color`, `cell` |
| 52 | `post-wall` | A wall of tiny tiles fills in behind you while a counter runs up | `total`, `label`, `days`, `cols`, `height`, `y`, `look` (`blueprint`) |
| 53 | `letter-dive` | Full screen: a word types on paper with the video inside the letters, then the camera dives through one letter | `text`, `into` (letter), `zoom`, `ink` |
| 54 | `layer-explode` | Full screen: the shot pulls apart into glass sheets in 3D (room, type, you, sound) | `text` (two words with `\|`), `angle`, `gap`, `plate` |
| 55 | `sketch-words` | The wall becomes paper and one word is sketched in pencil above your head | `text`, `small`, `color`, `width` |
| 56 | `blade-slice` | A diagonal cut: the top half slides off and snaps back | `angle`, `slide`, `at` |
| 57 | `head-stack` | Label chips drop and pile on your head, ride along, then tumble off | `text` (labels with `\|`) |
| 58 | `rack-focus` | Focus goes to the room (you go soft), then back to you (room soft) | `blur` |
| 59 | `banknote` | Full screen: a banknote with your face engraved in the oval and a number counting up | `text` (number), `title`, `serial`, `sub`, `ink` (hex), `crop` |
| 60 | `voice-note` | A voice-note bubble records and plays at the top, then shows Delivered | `text`, `seconds`, `x`, `y`, `width` |
| 61 | `impact-frame` | Full screen: a manga impact frame with ink, speed lines and one big word | `text`, `dark`, `y` |
| 62 | `dolly-zoom` | The room pushes in behind you while you stay the same size | `zoom` (1.4), `plate` |
| 63 | `press-front` | Full screen: a newspaper front page with your headline and a live halftone photo of you | `text` (headline), `sub`, `name`, `handle`, `date`, `crop` |
| 64 | `paper-tear` | That newspaper rips down the middle and falls away to reveal the shot | same as `press-front`, `hold` |
| 65 | `blow-away` | You turn to dust and blow away, leaving the empty room | `plate` (needed), `speed`, `wind`, `count` |

**Bonus and on-screen labels** (they don't add to the count):
- `comment-drop`: Big letters drop into a comment bar, the comment posts, a reply lands, the heart turns red. Options: `text` (keyword), `user`, `line`, `x`, `y`, `width`.
- `nameplate`: a "now playing" card at the bottom: a numbered name pill and a segment bar. `text` (names with `|`), `ticks` (start seconds with `|`), `bonus` (index shown as +), `hide` (`start-end` windows with `|`), `hud` (small tag top-left), `hud_at`, `color`, `y`, `x`.
- `tracklist`: an "in this video" list on the right that highlights the current effect. `text`, `ticks`, `more`, `more_at`, `scale`, `x`, `y`.
- `caption-pills`: caption pills, one line each. `text` (lines with `|`), `ticks` (seconds after the start), `bg` (hex per line with `|`), `y`, `x`, `size`.

**Named looks** (same effect, a fancier look; they don't add to the count):
- `glitter-spotlight` = `spotlight` with `look=sparkle`: the room goes dark, golden rays burst from behind your head, a big gold word with a shine sweep, twinkling sparkles and a glow around you. `text` (the word), `color`, `push`.
- `cover-star` with `look=editorial`: a soft warm film look, a classic serif masthead behind your head, an issue line and elegant cover lines. `text` (masthead), `issue`, `lines` (3 lines with `\|`), `right` (lines with `\|`), `color`, `accent`, `lines_y`, `right_y`.
- `liquid-glass-graph` with `look=bento`: the climbing graph moves to a smoked glass screen behind your head, with glass bento tiles in front of you (a donut, a KPI, bars). `text`, `from`, `to`, `donut` (`29%::label`), `kpi` (`672K::label`), `bars` (`197\|140\|124::label`).
- `apple-toggles` now sits above you, tucked behind your head, with a gentle zoom (`pos=below` for the old under-the-chin card; `overlap`, `zoom`).

Aliases work too: `bill`, `to-do`, `follow`, `stamp`, `countdown`, `cover`, `rain`, `pause`.

## Rules
- Never cover the face. Everything either goes behind the person or avoids the face by itself; if a check frame still shows text over the face, move it (`x`, `y`) or shorten the text.
- Effects run in the order listed. Put camera effects (`locked-on`, `lean-in`, `spotlight`) first when they overlap others.
- Zoom never goes past 2x, so the video stays sharp.
- This skill adds visuals only. Sound effects and captions are up to the user (CapCut works well).
- These are starter versions. Be honest about that if the user compares them to a reel they saw.
- Effects 46 to 65 are short by design: about 1 second each in a list reel, 1.5 to 3 seconds otherwise.
- Full-screen effects (`letter-dive`, `layer-explode`, `banknote`, `impact-frame`, `press-front`) hide a cut between two clips: put the cut inside them.
- Clean plate: `blow-away` needs `"plate": "<photo of the same shot without the person>"`. `dolly-zoom`, `layer-explode` and `live-cursor` look better with it. Ask the user for 2 seconds of the empty frame from the same tripod, then grab a frame: `ffmpeg -ss 1 -i empty.mp4 -frames:v 1 plate.jpg`. Without a plate these effects fill the gap from the surrounding wall, which only looks right on a plain wall. Put `blow-away` at the very end of the clip.
- In a plan, list `nameplate`, `tracklist` and `caption-pills` **last**. They hide themselves while a full-screen effect is on.
- A "many effects in a few seconds" reel: get the time of each spoken effect name with `scripts/words.py`, give each effect the window from its name to the next name, and add one `nameplate` (or `tracklist`) for the whole clip with `text` = the names and `ticks` = their start seconds.
- `scripts/preview.py <video> sheet.jpg [effect ...]` makes a quick sheet with three moments of each of effects 46 to 65.
