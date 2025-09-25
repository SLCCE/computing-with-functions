import turtle
import Character

class Board:
    def __init__(self, initialBoard):
        self.boardState = initialBoard
        self.rows = len(initialBoard)
        self.cols = len(initialBoard[0])
        self.bad_guy_turtle = turtle.Turtle()
        self.good_guy_turtle = turtle.Turtle()
        self.square_size = 75
        self.board_width = self.cols * self.square_size
        self.board_height = self.rows * self.square_size

        screen = turtle.Screen()
        screen.setup(self.board_width + 200, self.board_height + 200)
        turtle.speed(0)
        self.draw_board()
        self.draw_bad_guy(1, 1)
        self.draw_good_guy(2, 2)
        turtle.done()
    
    def draw_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                # offset so board is centered
                x = -self.board_width // 2 + j * self.square_size
                y = -self.board_height // 2 + i * self.square_size
                self.draw_square(x, y, self.boardState[i][j])
        
    def draw_square(self, x, y, fill):
        if (fill):
            turtle.fillcolor("black")
            turtle.begin_fill()
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            for _ in range(4):
                turtle.fd(self.square_size)
                turtle.left(90)
            turtle.end_fill()
        else:
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            for _ in range(4):
                turtle.fd(self.square_size)
                turtle.left(90)
    
    def draw_bad_guy(self, row, col):
        t1 = self.bad_guy_turtle
        t1.clear()
        # compute center of grid cell
        x = -self.board_width // 2 + col * self.square_size + self.square_size // 2
        y = -self.board_height // 2 + row * self.square_size + self.square_size // 2
        t1.up()
        t1.goto(x, y - 30)  # offset so circle is centered
        t1.down()
        t1.color("red")
        t1.circle(30)
        t1.color("black")

    def draw_good_guy(self, row, col):
        x = -self.board_width // 2 + col * self.square_size + self.square_size // 2
        y = -self.board_height // 2 + row * self.square_size + self.square_size // 2
        turtle.up()
        turtle.goto(x, y - 30)
        turtle.down()
        turtle.color("yellow")
        turtle.circle(30)
        turtle.color("black")

test = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]

Board(test)
