# loading into the player's state:
from characters import Character, Player

import turtle
t = turtle.Turtle()

inputInventory = []
with open("maps/inventory1.txt", "r") as fin:
    for line in fin.readlines():
        name, offense = line.split()
        inputInventory.append((name, offense))

inputEquipment = []
with open("maps/equipment1.txt", "r") as fin:
    for line in fin.readlines():
        name, defense, armorType = line.split()
        inputEquipment.append((name, defense, armorType))

p = Player(7, 10, 1, 1, inputInventory, inputEquipment, t)
print(p.inventory, p.equipment)
