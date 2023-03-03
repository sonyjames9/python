import turtle as t
from random import choice
ammu = t.Turtle()

num_sides = 5

colors = ["CornflowerBlue", "DarkGreen", "Indigo",
          "DeepSkyBlue", "LightSeaGreen", "Wheat", "Gray", "Pink"]


def draw_shape(num_sides):
  angle = 360/num_sides

  for _ in range(num_sides):
    ammu.forward(50)
    ammu.right(angle)


for shape_size_n in range(3, 11):
  color = choice(colors)
  ammu.color(color)
  colors.remove(color)
  draw_shape(shape_size_n)
