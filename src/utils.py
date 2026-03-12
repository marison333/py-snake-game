import time

def slow_print(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.03)
    print()