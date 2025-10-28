import turtle

from board import Board
import characters
import items
from ItemLoading import initalizePlayer

MAP_1_PATH = "maps/map1.txt"
status = ''

def state_checks():
    for badGuy in badGuys:
        if badGuy.get_position() == player.get_position():
            # Enter combat
            print("In Combat")

    if (player.get_hp() == 0):
        player.die()
        print("Player Died")
        return -1

def up():
    print('Moving up')
    player.move_up()
    player._draw_self('blue')
    status = state_checks()
    screen.update()

def down():
    print('Moving down')
    player.move_down()
    player._draw_self('blue')
    status = state_checks()
    screen.update()

def right():
    print('Moving right')
    player.move_right()
    player._draw_self('blue')
    status = state_checks()
    screen.update()

def left():
    print('Moving left')
    player.move_left()
    player._draw_self('blue')
    status = state_checks()
    screen.update()




screen = turtle.Screen()
screen.tracer(0)

board = Board.Board(MAP_1_PATH)
badGuys = []
loot = []
player = initalizePlayer()

board.draw_board()
screen.listen()

screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(right, 'Right')
screen.onkey(left, 'Left')



screen.mainloop()


    