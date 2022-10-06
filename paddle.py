from turtle import Turtle

PADDLEWIDTH = 20
PADDLEHEIGHT = 100


class Paddle(Turtle):
    def __init__(self, startx, starty):
        super().__init__()
        self.width = PADDLEWIDTH
        self.height = PADDLEHEIGHT
        self.startx = startx
        self.starty = starty
        self.penup()
        self.shape('square')
        self.resizemode('user')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(startx, starty)
        self.pos = self.position()

    def moveup(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def movedown(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)
