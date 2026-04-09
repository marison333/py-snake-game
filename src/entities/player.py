from entities.entities import Entity

class Player(Entity):
    def __init__(self, name: str, health: int, inventory: list):
        super().__init__(name, health)
        self.inventory = inventory