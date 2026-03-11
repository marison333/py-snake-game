# class for anything that exist in the game
class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health = self.health - amount

    def attack(self, target):
        target.take_damage(10)

# child classes that makes use of the class Entity and then adds its own stuff
# player has name, health and inventory
class Player(Entity):
    def __init__(self, name, health, inventory):
        super().__init__(name, health)
        self.inventory = inventory
        
# monster has name, health and loot
class Monster(Entity):
    def __init__(self, name, health, loot):
        super().__init__(name, health)
        self.loot = loot

