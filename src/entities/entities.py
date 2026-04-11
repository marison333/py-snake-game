# class for anything that exist in the game
# could be player, monster, npc, etc
class Entity:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.max_health = health

    def __str__(self) -> str:
        return self.name

    def take_damage(self, amount: int):
        self.health = self.health - amount

    def attack(self, target):
        target.take_damage(10)