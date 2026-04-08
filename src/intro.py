import time
from utils import slow_print
from create_player import create_player

title_file_path = 'assets/title.txt'


def intro():
    with open(title_file_path, 'r') as file:
        slow_print(file.read())

    slow_print("\nWelcome to Valoria, the capital of this Kingdom.\n")

    player = create_player()

    quest = input("\nIt appears you are a traveling Hero seeking a quest correct? (yes/no)\n").lower()
    if quest != "yes":
        slow_print("\nSafe travels adventurer.")
        exit()

    slow_print("\nThere is a Dungeon called the Crypt of the Forgotten King here in this Kingdom.")
    slow_print("Hidden treasures lie inside... and perhaps an ultra rare artifact.")

    journey = input("\nWould you like to know where this Dungeon is? (yes/no) ").lower()
    if journey != "yes":
        slow_print("\nThat's too bad, have a good day!")
        exit()

    slow_print("\nHead South towards the entrance of the capital.")
    slow_print("Guides there can lead you to the dungeon.")
    slow_print("\nWhile heading to the entrance you notice a small shop for weapons and armor.")

    shop = input("\nWould you like to go inside or continue? (inside/continue) ").lower()
    if shop == "inside":
        slow_print("\nYou enter the shop hoping to buy armor...")
        slow_print("But you quickly realize you have no gold.")
        slow_print("Embarrassed, you leave the shop.")
    else:
        slow_print("\nYou continue toward the capital entrance.")

    slow_print("\nYou finally arrive at the entrance where a guide waits.")

    crypt = input("\nThe guide asks: Are you the Hero seeking the Crypt? (yes/no) ").lower()
    if crypt != "yes":
        slow_print("\nAh... my mistake. Safe travels.")
        exit()

    slow_print("\nYou begin the long walk through the forest.")
    slow_print("\nAfter hours of travel, the entrance of the Crypt stands before you.")
    slow_print("\nAncient stone doors covered in runes tower above you.")

    enter = input("\nDo you enter the Crypt? (yes/no) ").lower()
    if enter != "yes":
        slow_print("\nYou decide this dungeon is too dangerous for now.")
        exit()

    slow_print("\nYou slowly step inside the dark Crypt...")
    slow_print("\nTorches flicker along the cold stone walls.")
    slow_print("\nSuddenly... bones begin rattling nearby.")

    time.sleep(1)

    slow_print("\nA Skeleton Warrior rises from the ground!")
    slow_print("\nYour first battle begins!")

    return player


if __name__ == "__main__":
    intro()