import time
from utils import slow_print

def outro(result, player):
    if result == "won":
        slow_print("\nThe skeleton collapses into a pile of bones.")
        slow_print("You find an Ancient Bone Sword among the remains!")

        # adds item to inventory
        player.inventory.append("Ancient Bone Sword")
        
        slow_print("\nYou grip the Ancient Bone Sword tightly.")
        slow_print("The crypt grows silent once again.")
        slow_print("\nYou walk deeper into the crypt for a short time...")
        slow_print("But an overwhelming dark presence can be felt deeper within the dungeon.")
        slow_print("\nPerhaps this place holds far greater dangers.")
        slow_print("You decide it would be wise to prepare before going further.")
        slow_print("\nYou turn around and make your way back to the entrance of the crypt.")
        slow_print("\nFresh air fills your lungs as you step outside.")
        slow_print("The sun slowly rises above the Kingdom of Valoria.")
        slow_print("\nYour adventure has only just begun...")

        time.sleep(2)
        slow_print("\nTO BE CONTINUED...")
    elif result == "lost":
        slow_print("\nThe skeleton defeats you.")
        time.sleep(2)
        slow_print("\nGAME OVER")
    elif result == "fled":
        slow_print("\nYou escape the crypt entrance.")
        slow_print("Perhaps you should prepare better before returning.")