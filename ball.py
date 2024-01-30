from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x_move=10
        self.y_move=10
        self.start()

    def paddle_bounce(self):
        self.y_move*=-1.04

    def brick_bounce(self, speed):
        self.y_move*=-1-speed
    def wall_bounce(self):
        self.x_move*=-1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def start(self):
        self.setheading(270)
        self.forward(10)

    def respawn(self):
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
