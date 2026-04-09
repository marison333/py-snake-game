from entities.entities import Entity

class Monster(Entity):
    def __init__(self, name: str, health: int, loot: list):
        super().__init__(name, health)
        self.loot = loot