import time

def slow_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)
    print()

def ask_choice(question, options):
    while True:
        choice = input(f"\n{question} ({'/'.join(options)}): ").lower().strip()
        if choice in options:
            return choice
        print("Invalid choice, please try again.")


def print_screen(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        print(file.read())


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