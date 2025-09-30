# Health potion item that tracks the amount it heals by and quanity.
class HealthPotion:
    def __init__(self, healAmount, quantity):
        self.healAmount = healAmount
        self.quantity = quantity
    
    # Checks that there is enough quanity to use if so returns healAmount otherwise return -1
    def use(self):
        if self.quantity < 1:
            return -1
        else:
            self.quantity -= 1
            return self.healAmount
