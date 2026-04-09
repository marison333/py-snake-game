from intro import intro
from outro import outro
from entities import Monster
from combat import fight

# define the player & Starts the intro
player = intro()

if player is None:
    print("You chose to leave Valoria. Maybe next time!")
    exit()

# define the monster
skeleton = Monster("Skeleton Warrior", 60, ["Ancient Bone Sword"])

# starts combat system
result = fight(player, skeleton)

# starts outro
outro(result, player)