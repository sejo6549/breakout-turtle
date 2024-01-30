from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.4, stretch_len=4)
        self.penup()
        self.goto(0, -220)

    def go_right(self):
        self.new_x=self.xcor()+20
        self.goto(self.new_x, self.ycor())

    def go_left(self):
        self.new_x=self.xcor()-20
        self.goto(self.new_x, self.ycor())

    def half(self):
        self.shapesize(stretch_wid=0.4, stretch_len=2)

    def return_to_normal(self):
        self.shapesize(stretch_wid=0.4, stretch_len=4)