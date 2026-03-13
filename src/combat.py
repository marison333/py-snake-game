import time
import random
from utils import slow_print
from entities import Player, Monster

john = Player("You", 100, [])
skeleton = Monster("Skeleton", 50, "Bones")

def print_status(player, monster):
    max_player_health = player.max_health
    max_monster_health = monster.max_health

    print("\n" + "=" * 40)
    print(f"  {player.name:<20} HP: {player.health if player.health > 0 else 0}/{max_player_health}")
    print(f"  {monster.name:<20} HP: {monster.health if monster.health > 0 else 0}/{max_monster_health}")
    print("=" * 40)
    
def print_action(message):
    slow_print(f">> {message}")

def roll_dice(sides=20):
    return random.randint(1, sides)

def resolve_attacker(attacker, defender):
    attack_roll = roll_dice(20)
    crit = attack_roll == 20
    fumble = attack_roll == 1
    hit_threshold = 10

    if fumble:
        print_action(f"{attacker.name} fumbles and does not land an attack!")
        return False

    if attack_roll >= hit_threshold or crit:
        base_damage = random.randint(5, 15)
        damage = base_damage * 2 if crit else base_damage
        defender.take_damage(damage)
        if crit:
            print_action(f"Critical hit! {attacker.name} slams {defender.name} for {damage} damage.\n\n")
        else:
            print_action(f"{attacker.name} hits {defender.name} for {damage} damage.")
        return True
    else:
        print_action(f"{attacker.name} misses {defender.name} (roll: {attack_roll}).")
        time.sleep(2)
        return False

def attempt_flee(player, monster):
    flee_roll = roll_dice(20)
    flee_threshold = 15
    if flee_roll >= flee_threshold:
        print("\033[H\033[J", end="")
        print_action(f"{player.name} successfully flees from {monster.name}!")
        time.sleep(2)
        return True

    print("\033[H\033[J", end="")
    print_action(f"{player.name} attempts to flee but fails (roll {flee_roll}).")
    print_action(f"{monster.name} takes advantage of the opening!")
    time.sleep(2)
    resolve_attacker(monster, player)
    return False

def fight(player, monster):
    fight_result = None

    slow_print("Combat starts!")

    while player.health > 0 and monster.health > 0:
        action = None
        while action not in ["attack", "flee"]:
            time.sleep(2)
            print("\033[H\033[J", end="")
            print_status(player, monster)
            print("\n")
            action = input("Choose action [attack/flee]: ").strip().lower()

        if action == "flee":
            if attempt_flee(player, monster):
                return
            if player.health <= 0:
                print("\033[H\033[J", end="")
                print_action(f"{player.name} have fallen in battle!")
                time.sleep(2)
                break
            continue

        # Player attack phase
        resolve_attacker(player, monster)
        if monster.health <= 0:
            print("\033[H\033[J", end="")
            print_action(f"{monster.name} is defeated!")
            time.sleep(2)
            break

        # Monster retaliates
        resolve_attacker(monster, player)
        if player.health <= 0:
            print("\033[H\033[J", end="")
            print_action(f"{player.name} has fallen in battle!")
            time.sleep(2)
            break

    print_status(player, monster)
    if player.health > 0 and monster.health <= 0:
        print("\033[H\033[J", end="")
        print_action(f"{player.name} win the fight!")
        time.sleep(2)
        fight_result = "won"
    elif player.health > 0:
        print("\033[H\033[J", end="")
        print_action(f"{player.name} escape the fight!")
        time.sleep(2)
        fight_result = "fled"
    else:
        print("\033[H\033[J", end="")
        print_action(f"{monster.name} wins the fight!")
        time.sleep(2)
        fight_result = "lost"

    return fight_result

if __name__ == '__main__':
    fight(john, skeleton)