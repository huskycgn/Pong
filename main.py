from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)

STARTX_R = 350
STARTY_R = 0

STARTX_L = STARTX_R * -1
STARTY_L = STARTY_R

r_paddle = Paddle(STARTX_R, STARTY_R)
l_paddle = Paddle(STARTX_L, STARTY_L)
running = True

while running:

    screen.update()
    screen.listen()

    screen.onkey(key='Up', fun=r_paddle.moveup)
    screen.onkey(key='Down', fun=r_paddle.movedown)
    screen.onkey(key='w', fun=l_paddle.moveup)
    screen.onkey(key='s', fun=l_paddle.movedown)


screen.exitonclick()