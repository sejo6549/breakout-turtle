import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from brick import BrickGenerator
from scoreboard import Scoreboard

ball=Ball()
paddle=Paddle()


#Setup screen
screen=Screen()

screen.setup(width=400, height=600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
bricks=BrickGenerator()
score=Scoreboard(0, 0, 3)
#---------------------------------

#Paddle movement events
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
#--------------------------------------

has_been_touched=False
halved_paddle=False

#Main loop
while(score.lives>0):
    if(not has_been_touched):
        ball.start()
    else:
        ball.move()
    if(ball.ycor()<-280):
        score.lose_a_life()
        ball.respawn()
        paddle.return_to_normal()
        has_been_touched=False
        halved_paddle=False

    if(ball.xcor()>180 or ball.xcor()<-180):
        ball.wall_bounce()
    if(ball.distance(paddle)<25 or ball.ycor()>280):
        has_been_touched=True
        ball.paddle_bounce()
    for brick in bricks.bricks:
        if(ball.distance(brick)<20):
            if(brick.bcolor=='red' and not halved_paddle):
                halved_paddle=True
                paddle.half()
            ball.brick_bounce(brick.speed)
            bricks.delete_brick(brick)
            score.update_score(brick.points)

    time.sleep(0.1)
    screen.update()

ball.hideturtle()
for brick in bricks.bricks:
    brick.hideturtle()
paddle.hideturtle()
screen.update()
screen.exitonclick()