from turtle import Turtle, Screen
import random
import os

t1 = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title='Make your bet', prompt='Which turle will win the race? Enter a color :')
os.system('cls || clear')
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
turtles = []

val = 120
for id in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[id])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=val)
  turtles.append(new_turtle)
  val = val - 40
# print(user_bet)

is_race_on = False
if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"Your turtle {winning_color} has won!")
      else:
        print(f"You lost! the {winning_color} turtle has won!")
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)


screen.exitonclick()
