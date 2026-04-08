from entities import Player
from utils import slow_print


def create_player():
    slow_print("Hero, what is your name? ") 
    name = input("> ")
    
    return Player(name, 100, [])


if __name__ == "__main__":
    player = create_player()
    print(f"Welcome, {player.name}! Your adventure begins now.")