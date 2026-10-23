# Alex's Cave Rescue

A cave adventure platformer for Alex (ages 7–8). Play: https://howibrettyourmother.github.io/alex-cave-rescue/

Five zones, each with a boss that grants a new power:
1. Crystal Cave — Boulder Bob → Double Jump
2. Mushroom Grotto — Batzilla → Super Dash (smash cracked walls)
3. Spider Depths — Queen Webby → Glow Light (reveal hidden platforms) · rescue **Mom**
4. Frozen Dark — Frosty Yeti → Fireball (burn wooden barriers)
5. Lava Core — King Magmor (3 phases) · rescue **Dad** · Lava Chicken!

Checkpoints, 5 hearts, no permanent loss, progress saved locally. All sounds are synthesized with WebAudio.
Build: `python3 src/build.py` (inlines src/game.js into index.html). Test: `python3 src/test.py` (Playwright WebKit).
