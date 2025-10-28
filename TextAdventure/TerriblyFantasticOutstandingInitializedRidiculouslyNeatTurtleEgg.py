import turtle

from board import Board
import characters
import items
from ItemLoading import initalizePlayer
from enum import Enum

MAP_1_PATH = "maps/map1.txt"
PLAYER_COLOR = 'blue'
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
def up():
    player.move_up()
    print(f'Moving up to {player.get_position()}')
    player._draw_self(PLAYER_COLOR)
    state_checks()
    screen.update()

def down():
    player.move_down()
    print(f'Moving down to {player.get_position()}')
    player._draw_self(PLAYER_COLOR)
    state_checks()
    screen.update()

def right():
    player.move_right()
    print(f'Moving right to {player.get_position()}')
    player._draw_self(PLAYER_COLOR)
    state_checks()
    screen.update()

def left():
    player.move_left()
    print(f'Moving left to {player.get_position()}')
    player._draw_self(PLAYER_COLOR)
    state_checks()
    screen.update()

def disableMovement():
    screen.onkey(doNothing, 'Up')
    screen.onkey(doNothing, 'Down')
    screen.onkey(doNothing, 'Right')
    screen.onkey(doNothing, 'Left')

def enableMovement():
    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')
    screen.onkey(right, 'Right')
    screen.onkey(left, 'Left')

def doNothing ():
    pass

####################################
# GAMEPLAY LOOP
####################################
screen = turtle.Screen()
screen.tracer(0)

board = Board.Board(MAP_1_PATH)
badGuys = []
loot = []
player = initalizePlayer()

board.draw_board()
screen.listen()

enableMovement()
screen.onkey(doNothing, 'space')



screen.mainloop()


    