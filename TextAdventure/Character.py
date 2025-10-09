from item.HealthPotion import *

class Character:
    def __init__(self, current_hp, max_hp, initX, initY):
        self.hp = [current_hp, max_hp]
        self.inventory = {"items": [HealthPotion(max_hp / 2, 1)]}
        self.xPos = initX
        self.yPos = initY
    
    # Heals the Character if they have a HealthPotion in their inventory, upto their max health. Returns the amount of health healed
    def heal(self):
        # Check for HealthPotions in character's inventory
        for item in self.inventory["items"]:
            if isinstance(item, HealthPotion):
                healedAmount = item.use()
                if healedAmount > -1:
                    # Prevent healing past the max hp of the character
                    healedAmount = min(healedAmount, self.hp[1] - self.hp[0])
                    self.hp[0] += healedAmount
                    return healedAmount
        return -1