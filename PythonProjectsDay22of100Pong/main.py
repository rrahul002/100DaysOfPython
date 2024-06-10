from turtle import Screen, Turtle, screensize
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Rahul's Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = 1

while game_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce()
  if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
    ball.paddlebounce()
  if ball.xcor() >= 400:
    ball.reset()
    scoreboard.left_scoring()
  elif ball.xcor() <= -400:
    ball.reset()
    scoreboard.right_scoring()



screen.exitonclick()