# loading into the player's state:
from characters import Character, Player, BadGuy
from pathlib import Path

import turtle

TILE_SIZE = 75

def initalizePlayer(boardWidth, boardHeight):
    t = turtle.Turtle()

    project_root = Path(__file__).resolve().parent
    invPath = (project_root / "maps/map1/inventory1.txt").resolve()
    eqPath = (project_root / "maps/map1/equipment1.txt").resolve()

    inputInventory = []
    with open(invPath, "r") as fin:
        for line in fin.readlines():
            name, offense = line.split()
            inputInventory.append((name, offense))

    inputEquipment = []
    with open(eqPath, "r") as fin:
        for line in fin.readlines():
            name, defense, armorType = line.split()
            inputEquipment.append((name, defense, armorType))

    p = Player(7, 10, 1, 1, inputInventory, inputEquipment, t, (boardWidth, boardHeight), TILE_SIZE)
    print(p.inventory, p.equipment)
    return p

def initializeEntities(levelNumber, boardWidth, boardHeight):
    project_root = Path(__file__).resolve().parent
    pathString = "maps/map" + str(levelNumber) + "/entity" + str(levelNumber) + ".txt"

    entityPath = (project_root / pathString).resolve()
    entityList = []
    with open(entityPath, "r") as fin:
        for line in fin.readlines():
            entity, curHp, maxHp, x, y = line.split()
            if (entity == 'bad'):
                t = turtle.Turtle()
                badGuy = BadGuy(int(curHp), int(maxHp), int(x), int(y), [], [], t, (boardWidth, boardHeight), TILE_SIZE)
                entityList.append(badGuy)
            # entityList.append((entity, int(curHp), int(maxHp), int(x), int(y)))            
    return entityList
