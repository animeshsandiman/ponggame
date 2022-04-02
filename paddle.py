from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(position)
        self.up()
        self.down()







    def up(self):
        new_y = self.ycor() + 20
        self.goto(Paddle.xcor(self), new_y )

    def down(self):
        new_y = self.ycor() - 20
        self.goto(Paddle.xcor(self), new_y)