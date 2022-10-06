from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move(self, player):
        if player == 'r':
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
        elif player == 'l':
            new_x = self.xcor() - self.x_move
            new_y = self.ycor() - self.y_move
            print('linker Spieler fängt an!')
        self.goto(new_x, new_y)
        print(self.xcor())

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)