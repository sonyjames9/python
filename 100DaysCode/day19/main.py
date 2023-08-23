from hashlib import new
from turtle import Turtle, Screen

ammu = Turtle()
screen = Screen()


def move_forward():
  ammu.forward(20)


def move_backward():
  ammu.backward(20)


def move_left():
  new_heading = ammu.heading() + 90
  ammu.setheading(new_heading)


def move_right():
  new_heading = ammu.heading() - 90
  ammu.setheading(new_heading)


def clear_screen():
  ammu.clear()
  ammu.penup()
  ammu.home()
  ammu.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
