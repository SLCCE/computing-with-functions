import turtle
from Character import Character
# from item.HealthPotion import HealthPotion

class Player(turtle.Turtle, Character):
    def __init__(self, current_hp, max_hp, start_x, start_y, startingInventory, startingEquipment, tile_size=24):
        # initializing turtle
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.penup()
        self.speed(0)
        
        # initializing character for hp and inventory
        Character.__init__(self, current_hp, max_hp, start_x, start_y, startingInventory, startingEquipment)
        
        # player position and settings
        self.tile_size = tile_size
        
        self._draw_player()
    
    def __str__(self):
        return str(self.hp)
    
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
        self.goto(x * self.tile_size, y * self.tile_size)
        self._draw_player()
    
    # equipment methods
    def equip_item(self, slot, item):
        if slot in self.equipment:
            self.equipment[slot] = item
    
    def unequip_item(self, slot):
        if slot in self.equipment:
            self.equipment[slot] = None
    
    # inventory methods
    def add_item(self, item):
        self.inventory["items"].append(item)
    
    def remove_item(self, item):
        if item in self.inventory["items"]:
            self.inventory["items"].remove(item)
    
    def use_item(self, item_index):
        if 0 <= item_index < len(self.inventory["items"]):
            item = self.inventory["items"][item_index]
            if isinstance(item, HealthPotion):
                healed = self.heal()
                if healed > 0:
                    return "Healed " + str(healed) + " HP!"
        return "Invalid item!"
    
    # move methods
    def move_up(self, board):
        new_x = self.position[0]
        new_y = self.position[1] + 1
        self.set_position(new_x, new_y)
    
    def move_down(self, board):
        new_x = self.position[0]
        new_y = self.position[1] - 1
        self.set_position(new_x, new_y)
    
    def move_left(self, board):
        new_x = self.position[0] - 1
        new_y = self.position[1]
        self.set_position(new_x, new_y)
    
    def move_right(self, board):
        new_x = self.position[0] + 1
        new_y = self.position[1]
        self.set_position(new_x, new_y)

if __name__ == "__main__":
    p = Player(7, 10, 1, 1, [], [])
    print(p)
