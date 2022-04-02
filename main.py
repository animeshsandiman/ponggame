from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scorebord import Scorebord
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)



pad_a = Paddle((350, 0))
pad_b = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(pad_a.up, "Up")
screen.onkey(pad_a.down, "Down")
screen.onkey(pad_b.up, "w")
screen.onkey(pad_b.down, "s")
scorebord = Scorebord()
is_game_on = True

while is_game_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(pad_a) < 50:
        ball.bounce_x()


    if ball.xcor() > 400:
        ball.restart_x()
        scorebord.l_points()

    if ball.xcor() < -320 and ball.distance(pad_b) < 50:
        ball.bounce_x()


    if ball.xcor() < -400:
        ball.restart_y()
        scorebord.r_points()















screen.exitonclick()
