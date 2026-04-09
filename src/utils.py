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
    with open(file_path, 'r') as file:
        print(file.read())