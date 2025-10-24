# from item.HealthPotion import *
import turtle

class Character:
    def __init__(self, current_hp, max_hp, initX, initY, startingInventory, startingEquipment, t: turtle.Turtle):
        self.hp = [current_hp, max_hp]
        self.xPos = initX
        self.yPos = initY
        # self.inventory = {"items": [HealthPotion(max_hp / 2, 1)]}
        self.inventory = startingInventory
        self.equipment = startingEquipment
        self.t = t
    
    def _draw_self(self, color):
        pass
    
    def die(self):
        self.t.clear()
    
    def __str__(self):
        return str(type(self)) + " " + str(self.hp)
    
    # hp getters and setters
    def get_hp(self):
        return self.hp[0]
    
    def set_hp(self, value):
        self.hp[0] = min(value, self.hp[1])
        if self.hp[0] < 0:
            self.hp[0] = 0
    
    def get_max_hp(self):
        return self.hp[1]
    
    def set_max_hp(self, value):
        self.hp[1] = value
    
    # position getters and setters
    def get_position(self):
        return self.position
    
    def set_position(self, x, y):
        self.position = [x, y]
    
    # Heals the Character if they have a HealthPotion in their inventory, upto their max health. Returns the amount of health healed
    # def heal(self):
    #     # Check for HealthPotions in character's inventory
    #     for item in self.inventory["items"]:
    #         if isinstance(item, HealthPotion):
    #             healedAmount = item.use()
    #             if healedAmount > -1:
    #                 # Prevent healing past the max hp of the character
    #                 healedAmount = min(healedAmount, self.hp[1] - self.hp[0])
    #                 self.hp[0] += healedAmount
    #                 return healedAmount
    #     return -1
