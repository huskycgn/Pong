import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

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
ball = Ball()
running = True
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=r_paddle.moveup)
screen.onkey(key='Down', fun=r_paddle.movedown)
screen.onkey(key='w', fun=l_paddle.moveup)
screen.onkey(key='s', fun=l_paddle.movedown)
nextplayer = 'r'

while running:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move(nextplayer)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390 or ball.xcor() < -390:
        sleep(1)
        if ball.xcor() > 0:
            ball.reset()
            nextplayer = 'l'
            scoreboard.l_point()
        else:
            ball.reset()
            nextplayer = 'r'
            scoreboard.r_point()
    screen.update()

screen.exitonclick()
