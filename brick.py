from turtle import Turtle

COLORS=['red', 'orange', 'yellow', 'green']
class BrickGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks=[]
        self.level=1
        self.hideturtle()
        self.generate()

    def generate(self):
        i=0
        for color in COLORS:
            for x in range(9):
                brick=Turtle(shape='square')
                brick.bcolor=color
                brick.color(color)
                brick.points=20*(3+self.level-i)
                brick.speed=0.02*(2+self.level-i)
                brick.shapesize(stretch_wid=0.4, stretch_len=1.5)
                brick.penup()

                brick.goto(-160+x*40, 280-i*20)
                self.bricks.append(brick)
            i+=1

    def delete_brick(self, brick):
        brick.clear()
        brick.hideturtle()
        if brick in self.bricks:
            self.bricks.remove(brick)

    def level_up(self):
        self.level+=1
        self.generate()