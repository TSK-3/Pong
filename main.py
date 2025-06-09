from turtle import *
import time
from pad import paddle
from ball import Ball
from score_board import Scoreboard
t= Turtle()
s = Screen()

s.setup(800,600)
s.bgcolor("black")
s.title("Pong Game")
s.tracer(0) # Turns off the screen updates until the paddle reaches the required position


ball = Ball()
score = Scoreboard()


r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))

s.listen()
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")
s.onkey(r_paddle.go_up,"Up")    
s.onkey(r_paddle.go_down,"Down")
game_is_on = True

while game_is_on:

    
    time.sleep(ball.move_Speed)
    s.update()
    ball.move()
   

    if ball.ycor() > 280 or ball.ycor() < -280 :      # collision
        ball.bounce_y()



    if ((ball.xcor() > 320 or ball.xcor() <-320) and ((ball.distance(r_paddle))< 50 or (ball.distance(l_paddle) < 50))):
        ball.bounce_x   ()



    if ball.xcor() > 380  :
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()



    


s.exitonclick()