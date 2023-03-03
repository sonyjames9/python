import turtle as t
from random import choice

ammu = t.Turtle()
# ammu.colormode(255)
colors = ["CornflowerBlue", "DarkGreen", "Indigo",
          "DeepSkyBlue", "LightSeaGreen", "Wheat", "Gray", "Pink"]

# ammu.colormode(255)
directions = [1, 90, 180, 270]
ammu.pensize(10)
ammu.speed("fastest")

for _ in range(200):
  ammu.color(choice(colors))
  ammu.forward(30)
  ammu.setheading(choice(directions))

import
