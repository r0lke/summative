# Combo Arena — Development TODO

## Phase 1 — Data & Structures
- [ ] Define a single attack structure: `id`, `name`, `energy_cost`, `damage`
- [ ] Create a starter set of 5–7 attacks with varied cost/damage ratios
- [ ] Define player structure: `max_energy`, `current_energy`, `unlocked_attacks[]`, `hp`
- [ ] Define enemy structure: `name`, `max_hp`, `current_hp` (randomized per encounter)
- [ ] Define a Turn context object: `enemy_hp`, `player_energy`, `available_attacks[]`

---

## Phase 2 — Knapsack DP Algorithm (core mechanic)
- [ ] Implement basic 0/1 knapsack DP: `dp[e]` = max damage at energy budget `e`
- [ ] Add backtracking to recover the list of chosen attacks from the knapsack DP table
- [ ] Write unit tests: zero energy, single attack, all cheap, exact budget fit
- [ ] Enforce the rule: each attack can be used at most once per turn (0/1 knapsack constraint)
- [ ] *(Optional)* Add unbounded knapsack mode as a separate flag if repeats are allowed

---

## Phase 3 — Game Logic
- [ ] Implement turn loop: `player_turn()` → `enemy_turn()` → `check_win()` → `next_round()`
- [ ] Implement `apply_combo(attacks[])`: sum damage, reduce enemy HP, spend energy
- [ ] Implement simple enemy AI: fixed or randomized damage per turn
- [ ] Implement win/loss conditions: `enemy.hp <= 0` → win; `player.hp <= 0` → game over
- [ ] Implement attack unlock system: after each win, offer 1–2 new attacks to choose from
- [ ] Implement enemy generation: random HP in a range that grows each round
- [ ] Decide and implement energy restore rule: full restore vs partial between turns

---

## Phase 4 — UI
- [ ] Choose UI platform: console / HTML+JS / Tkinter / Pygame — lock in before starting
- [ ] Battle screen: show enemy HP bar and player energy counter, updated each turn
- [ ] Display available attacks with name, energy cost, and damage value
- [ ] Allow manual attack selection: click or type number; show running energy cost
- [ ] Add "Optimize" button: runs knapsack DP and highlights the optimal combo; player can accept or override
- [ ] Add "Attack" button: applies the chosen combo; disabled if energy is exceeded
- [ ] Add a battle log / event feed: `"You used Slash (cost 3) — enemy loses 18 HP"`
- [ ] Win / game over screen: show total damage dealt, offer unlock choice or restart

---

## Phase 5 — UX & Balance
- [ ] Playtest: complete 5 consecutive fights and check if difficulty ramps naturally
- [ ] Run knapsack DP on all attacks at max energy — verify no single attack is always dominant
- [ ] Ensure attack variety: fast-cheap, slow-heavy, and middle-ground options all see use
- [ ] Add minimal visual feedback on hit: HP flash, bar pulse, or a simple beep
- [ ] *(Optional)* Save progress to a JSON file: unlocked attacks, current round
- [ ] Add a first-turn hint: `"Tip: press Optimize to find the best combo"`

---

## Phase 6 — Polish & Wrap-up
- [ ] Write a README: how to install, how to run, screenshot or GIF
- [ ] Comment the knapsack DP algorithm thoroughly — useful for portfolio and code review
- [ ] Refactor into modules: `dp.py` / `game_logic.py` / `ui.py` / `data.py`
- [ ] Final playtest with someone else — note any confusing moments and fix them
