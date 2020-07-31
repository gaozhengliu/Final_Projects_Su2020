# ZOOMBIE SURVIVAL GAME
-- A Monte Carlo Simulation on Can Human Survive
## Creator: GaoZheng Liu (netID: GL11)
### The backgroud story
There is a peacful town located on an isolated island, where 50,000 citzens happily live together. One night, an expected meteor shower hit the little town, turning 5,000 citizens to Zombies. Those zombies'only life goal is to attact the remaining humans and EAT them. Scratches and bites can turn humans into new zombies. Desperating humans picked up weapons to defend themselves and to eliminate zombies. Warning: zombies are afraid of the water, so they will not get close to the ocean. Can humans survive?
### Rules of the game
- The zombie attacts the human, either eat or change the human.
- The human fights against the zombie, either defend or eliminate the zombie.
- The game ends when the creature remains on the island is either all humans or all zombies.
### Variables
#### Independing Variables
- Static Threshold Variable: 
- initial zombies = 5,000 
- initial citizens = 45,000
- human's moving distance per day = 50, 000 meters
- zombie's moving distance per day = 5, 000 meters
- area of the island, a square 500, 000 * 500, 000 square meters
- where the human can be in the map: 500,000 * 500,000 square meters
- where the zombie can be in the map: 499,000 * 490,000 square meters 
- how far a zombie can find a human: 100 meters
- how far a human can find a zombie: 200 meters
- how far a human can shot a zombie if get a gun: 100 meters
- Random Variables:
- how likely a human and a zombie will enconter: 
- how likely a human will be attacked by one zombie: mean: 0.3, std: 0.1
- how likely a human will be infected by one zombie who starts the attack: mean: 0.5, std: 0.1
- how likely a human can collect the weapon that day: mean: 0.7, std: 0.1
- how many bullets in that particular collect: mean 10, std: 2
- how likely a human can eliminate a zombie: mean: 0.5, std 0.1

–	Change: the encounter rate,  the infection rate, the death rate
–	Change: ways people spread in the island
–	Random: How 5,000 zoombie spread in the island
#### Depending Variables
- Result: average of who wins at when the game end
