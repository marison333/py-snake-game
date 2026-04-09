import os
import json
from utils import slow_print, print_screen, ask_choice
from create_player import create_player

TITLE_SCREEN = 'assets/title.txt'
base_dir = os.path.dirname(__file__)
story_file_path = os.path.join(base_dir, 'story.json')


def load_story():
    with open(story_file_path, 'r') as file:
        return json.load(file)


def show_intro():
    print_screen(TITLE_SCREEN)

    slow_print("\nWelcome to Valoria, the capital of this Kingdom.\n")


def handle_choice(scene):
    for line in scene.get("text", []):
        slow_print(f"\n{line}")

    # Scene zonder keuze = gewoon tonen en door
    if not scene.get("options"):
        return None

    choice = ask_choice(scene["question"], scene["options"])

    for line in scene["results"].get(choice, []):
        slow_print(f"\n{line}")

    return choice


def play_intro_story(story):
    current_scene = story["start"]

    while current_scene:
        scene = story[current_scene]
        choice = handle_choice(scene)

        # scene zonder keuzes (zoals battle_start)
        if not scene.get("options"):
            return current_scene == "battle_start"

        # geen volgende scene = stop
        if "next" not in scene or not scene["next"]:
            return False

        current_scene = scene["next"].get(choice)

    return False


def intro():
    story = load_story()

    show_intro()
    player = create_player()

    reached_battle = play_intro_story(story)

    if not reached_battle:
        return None

    return player


if __name__ == "__main__":
    intro()