from turtle import Turtle, Screen


ammu_the_turtle = Turtle()
ammu_the_turtle.shape("turtle")
ammu_the_turtle.color("red")
ammu_the_turtle.shapesize(5.0, 5.0)
# ammu_the_turtle.forward(100)
# ammu_the_turtle.right(90)
# ammu_the_turtle.forward(100)

for _ in range(10):
  ammu_the_turtle.color("blue")
  ammu_the_turtle.forward(100)
  ammu_the_turtle.penup()
  ammu_the_turtle.right(90)
  ammu_the_turtle.forward(200)
  ammu_the_turtle.right(90)
  ammu_the_turtle.forward(200)
  ammu_the_turtle.pendown()


screen = Screen()
screen.exitonclick()
