import turtle

from board import Board
import characters
import items

MAP_1_PATH = "maps/map1.txt"

def state_checks():
    for badGuy in badGuys:
        if badGuy.get_position() == player.get_position():
            # Enter combat
            print("In Combat")

    if (player.get_hp[0] == 0):
        player.die()
        print("Player Died")
        return 

def up():
    player.move_up()
    player._draw_self()
    status = state_checks()
    screen.update()




screen = turtle.Screen()
screen.tracer(0)

board = Board.Board("maps/map1.txt")
badGuys = []
loot = []
player = characters.Player()

screen.listen()

screen.onkey(up, 'Up')



screen.mainloop()


    