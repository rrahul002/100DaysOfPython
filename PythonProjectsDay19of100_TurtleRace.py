from turtle import Turtle, Screen
import random

t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
t6 = Turtle(shape="turtle")
t7 = Turtle(shape="turtle")
t1.color("red")
t2.color("orange")
t3.color("yellow")
t4.color("green")
t5.color("blue")
t6.color("purple")
t7.color("black")
turtles= [t1, t2, t3, t4, t5, t6, t7]



screen = Screen()
screen.setup(width=500, height= 400)
money = 1

while money >= 0:
  is_race_on = True
  user_turtle = screen.textinput(title = "Make Your Bet!", prompt= "Which turtle will win? Enter color: ")
  user_bet = screen.textinput(title="Bet Amount", prompt="How much will you bet?")
  t1.penup()
  t2.penup()
  t3.penup()
  t4.penup()
  t5.penup()
  t6.penup()
  t7.penup()
  t1.goto(x=-230,y=150)
  t2.goto(x=-230,y=100)
  t3.goto(x=-230,y=50)
  t4.goto(x=-230,y=0)
  t5.goto(x=-230,y=-50)
  t6.goto(x=-230,y=-100)
  t7.goto(x=-230,y=-150)
  turtles.append(t1)

  odds = [1, 1, 1, 1, 1, 1, 1]

  if int(user_bet) <= money:
    money =- int(user_bet)
    print(f"You bet ${user_bet} on {user_turtle}!")
  else:
    print(f"You only have ${money}!")
    is_race_on = False
  winners = []
  while is_race_on:
    for turtle in turtles:
      if turtle.xcor() >= 230:
        winners.append(turtle)
      rand_distance = random.randint(0,10)
      turtle.forward(rand_distance)
      if len(winners) == 7:
        is_race_on = False
  #if winners[0] == user_turtle.lower():
    #money = user_bet * odds[winners[0]]
    
    
  

screen.exitonclick()
