items = ["x"] * 9
curItems = 0
# helmet, chestplate, leggings, boots
equipment = ["x"] * 4
equipmentSlotMap = {"helmet": 0, "chestplate": 1, "leggings": 2, "boots": 3}
with open("maps/item1.txt", "r") as fin:
    for line in fin.readlines():
        itemType, name, strength = line.split()
        strength = int(strength)
        if itemType == "equipment":
            equipment[equipmentSlotMap[name]] = (name, strength)
        # elif itemType == "weapon":
        else:
            items[curItems] = (name, strength)
            curItems += 1
        # else:
        #     raise Exception("not equipment or item")
print(equipment, items)
