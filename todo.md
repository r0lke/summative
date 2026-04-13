
### Setup
- [ ] Init pygame, game loop, state machine (`MENU` `BATTLE` `LEVEL_UP` `GAME_OVER`)

### Player
- [ ] `energy` — persists between fights
- [ ] `attacks` list — new attack unlocked every N enemies
- [ ] `gain_energy(amount)` and `add_attack(attack)`

### Enemy
- [ ] Random `health` scaling with wave number
- [ ] `energy_reward` — often less than needed to win next enemy

### Knapsack Core
- [ ] `solve(energy, attacks)` → optimal attack combo via DP
- [ ] capacity = current energy, items = attacks (cost/damage)
- [ ] `can_win(combo, enemy_hp)` check

### Battle
- [ ] Show enemy HP, player energy, available attacks
- [ ] Player picks attacks manually; DP suggests optimal combo
- [ ] Apply damage, check win/loss

### Progression
- [ ] Every N kills → unlock new attack
- [ ] Enemy HP and reward scale per wave

### UI
- [ ] HUD: energy, wave, attack list with cost/damage
- [x] Generate enemy picture
- [ ] Highlight DP-optimal selection
- [ ] Game over / win screens