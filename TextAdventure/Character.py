class Character:
    def __init__(self, current_hp, max_hp):
        self.hp = [current_hp, max_hp]
        self.inventory = {"items": []}