# ZOOMBIE SURVIVAL GAME
#### A Monte Carlo Simulation on Wheather  Human Can Survive
##### Creator: GaoZheng Liu (netID: GL11)

## The backgroud story
There is a peaceful town located on an isolated island, where 5 000 citizens happily live together. <br>
One night, an expected meteor shower hit the little town, turning 50 citizens to Zombies. <br>
Those zombies only life goal is to attack the remaining humans and EAT them. Scratches and bites can turn humans into new zombies. <br>
Desperating humans picked up weapons to defend themselves and to eliminate zombies. <br>
Can humans survive?

## Rules of the game
- The zombie attacts the human, either eat or change the human.
- The human fights against the zombie, either defend or eliminate the zombie.
- The game ends when the creature remains on the island is either all humans or all zombies.
## Survival Strategy
0. Humans are not able to defend themselves. Zombies randomly pick up the target, there are certain rates randomly generated to turn the target, eliminated by the target, escaped by the target, or eat the target.
1. Humans are randomly assigned ammo and randomly pick up zombie target for each bullet. Zombies act the same way.
2. Humans are randomly assigned ammo and shot firstly at the zombies who attack them. Zombies act the same way.
3. Humans rally in groups randomly. Zombies, instead pick up individual survivals, they pick up surviving groups.


## Variables
### Independing Variables
Initial Constant 
- Number of Citizens
- Number of Zombies
- Number of Ammo
- Choice of Strategy
- How deadly a zombie attack could be: aggregate of r
    - 0.8 < R <1: the poor person is eaten, very likely when surrounded by more than 1 zombie
    - 0.5 < R <0.8: the poor person is turned a zombie
    - 0.1 < R <0.5: the lucky person escaped
    - 0< R <0.1: the brave person kill the zombies.
### Random Variables
For Zombie:
- Randomly picked zombies from all citizens. Represented by UIN
- Randomly picked a survivor to attact by one zombie.
- Random rate of the impact of the attack, r belongs [0, 1] 
- f multiple zombies chose the same target, 1 - r1*r2*r….*rn
- In strategy 4, Randomly pick a survivor groups to attack
For Human:
- Randomly assigned for ammo.
- Randomly picked a zombie to shot for each bullet.
- Random shooting rate

### Depending Variables
- Winner: Human, Zombie: Only one side dominates the island
- Days: How long it take for one side to win

## Result

