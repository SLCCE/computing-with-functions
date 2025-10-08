from Item import Item
# Health potion item that tracks the amount it heals by and quanity.
class HealthPotion(Item):
    def __init__(self, name, quanity, healAmount):
        super().__init__(name, quanity)
        self.healAmount = healAmount

    def getHealAmount(self):
        return self.healAmount
    
    def setHealAmount(self, amount):
        self.healAmount = amount
    
    # Checks that there is enough quanity to use if so returns healAmount otherwise return -1
    def use(self):
        if self.quantity < 1:
            return -1
        else:
            self.quantity -= 1
            return self.healAmount
    
    def draw(self, xpos, ypos, scale):
        # TODO: draw potion
        return
