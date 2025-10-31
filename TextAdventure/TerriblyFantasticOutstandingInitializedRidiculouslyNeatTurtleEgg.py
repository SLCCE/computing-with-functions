import turtle

from board import Board
import characters
import items
from Loader import initalizePlayer, initializeEntities
from enum import Enum

LEVEL = 1
MAP_1_PATH = "maps/map2/map2.txt"
PLAYER_COLOR = 'green'
enemy = None

class Status(Enum):
    ERROR = -1
    MOVE = 1
    COMBAT = 2
    DEAD = 3

status = Status.ERROR


def state_checks():
    global status
    if (status == Status.DEAD):
        return
    elif (status == Status.COMBAT):
        return

    for badGuy in badGuys:
        if badGuy.get_position() == player.get_position():
            # Enter combat
            status = Status.COMBAT
            enemy = badGuy
            # Disable movement
            disableMovement()
            # Enable attack
            screen.onkey(attack, 'space')
            print("In Combat")

    
    
####################################
# COMBAT
####################################
def attack():
    global status
    print('Attacking')
    if (player.get_hp() == 0):
        player.die()
        print("Player Died")
        status = Status.DEAD
        return 



####################################
# MOVEMENT
####################################
def move (direction):
    playerPos = player.get_position()
    if (direction == 'up'):
        goalPos = board.get_tile(playerPos[0] + 1, playerPos[1])
        if (goalPos.getStatus() == Board.Tile.Status.REGULAR.value):
            player.move_up()
            print(f'Moving {direction} to {player.get_position()}')
        else:
            print(f'Goal Position is of type: {goalPos.getStatus()}')
    elif (direction == 'down'):
        goalPos = board.get_tile(playerPos[0] - 1, playerPos[1])
        if (goalPos.getStatus() == Board.Tile.Status.REGULAR.value):
            player.move_down()
            print(f'Moving {direction} to {player.get_position()}')
        else:
            print(f'Goal Position is of type: {goalPos.getStatus()}')
    elif (direction == 'right'):
        goalPos = board.get_tile(playerPos[0], playerPos[1] + 1)
        if (goalPos.getStatus() == Board.Tile.Status.REGULAR.value):
            player.move_right()
            print(f'Moving {direction} to {player.get_position()}')
        else:
            print(f'Goal Position is of type: {goalPos.getStatus()}')
    elif (direction == 'left'):
        goalPos = board.get_tile(playerPos[0], playerPos[1] - 1)
        if (goalPos.getStatus() == Board.Tile.Status.REGULAR.value):
            player.move_left()
            print(f'Moving {direction} to {player.get_position()}')
        else:
            print(f'Goal Position is of type: {goalPos.getStatus()}')
            
    player._draw_self(PLAYER_COLOR)
    state_checks()
    screen.update()

def disableMovement():
    screen.onkey(doNothing, 'Up')
    screen.onkey(doNothing, 'Down')
    screen.onkey(doNothing, 'Right')
    screen.onkey(doNothing, 'Left')

def enableMovement():
    # screen.onkey(up, 'Up')
    # screen.onkey(down, 'Down')
    # screen.onkey(right, 'Right')
    # screen.onkey(left, 'Left')
    screen.onkey(lambda: move('up'), 'Up')
    screen.onkey(lambda: move('down'), 'Down')
    screen.onkey(lambda: move('right'), 'Right')
    screen.onkey(lambda: move('left'), 'Left')

def doNothing ():
    pass

####################################
# GAMEPLAY LOOP
####################################
screen = turtle.Screen()
screen.tracer(0)

board = Board.Board(MAP_1_PATH)
print(board)
badGuys = []
loot = []
player = initalizePlayer(board.board_width // 2, board.board_height // 2)
entities = initializeEntities(1)
print(entities)

board.draw_board()
screen.listen()

enableMovement()
screen.onkey(doNothing, 'space')



screen.mainloop()


    