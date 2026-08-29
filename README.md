# Adventure Game

A simple text-based adventure game written in Python. Explore the wilderness, fight enemies, visit the shop, and try to survive as long as you can.

---

## Overview

Python Adventure is a lightweight console RPG where you create a hero, explore random locations, battle enemies, manage your inventory, and spend gold at the village shop. The game focuses on core RPG loops—exploration, combat, resource management—while remaining easy to run and modify.

---

## Features

- **Character creation** — Enter a custom hero name
- **Status tracking** — Health, gold, inventory, and current location
- **Exploration** — Random locations (forest, cave, river) with chance-based events
- **Turn-based combat** — Fight or run from enemies (goblin, wolf, bandit, skeleton)
- **Shop system** — Buy health potions and upgrade your weapon
- **Rest mechanic** — Recover health between adventures
- **Slow text output** — Typewriter-style narrative for immersion

---

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only standard library)

---

## How to Run

```bash
python adventure.py
```

Or:

```bash
python3 adventure.py
```

---

## How to Play

1. Enter your hero’s name
2. Choose an action from the menu:
   - **Explore** — Travel to a random location (may encounter enemies or find gold)
   - **Visit the shop** — Buy a Health Potion (25 gold) or Steel Sword (60 gold)
   - **Rest** — Recover a small amount of health
   - **Quit** — End the game and see your final gold
3. In combat, type `f` to fight or `r` to attempt escape
4. Survive as long as possible and collect gold

---

## Possible Improvements

- [ ] Save / load system
- [ ] More locations and enemy types
- [ ] Inventory usage (e.g. equip weapons, drink potions on demand)
- [ ] Experience points and leveling
- [ ] Random events and story encounters
- [ ] Better combat balancing

---

## License

MIT

---

Built as a simple demonstration of a text-based RPG loop in pure Python.
