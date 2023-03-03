# import colorgram

# rgb_colors = []
# colors = colorgram.extract('100DaysCode//day18-gui//color_pencil.jpg', 30)
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
ammu = turtle_module.Turtle()
ammu.speed("fastest")
ammu.penup()
ammu.hideturtle()

color_list = [(25, 99, 188), (172, 8, 51), (208, 163, 77), (21, 31, 64), (217, 62, 120), (1, 53, 35), (0, 197, 235), (212, 157, 7), (25, 49, 145), (181, 48, 95), (228, 217, 75), (10, 195, 143), (77, 11, 4), (246, 152, 196), (174, 74, 24),
              (7, 138, 105), (217, 125, 189), (234, 214, 6), (2, 105, 49), (141, 27, 18), (75, 9, 36), (236, 49, 33), (127, 208, 95), (99, 103, 191), (146, 215, 128), (2, 92, 105), (13, 189, 247), (246, 12, 18), (246, 12, 11), (90, 72, 2)]

ammu.setheading(225)
ammu.forward(300)
ammu.setheading(0)
number_of_dots = 180

for dot_count in range(1, number_of_dots+1):
  ammu.dot(20, random.choice(color_list))
  ammu.forward(50)

  if dot_count % 10 == 0:
    ammu.setheading(90)
    ammu.forward(50)
    ammu.setheading(180)
    ammu.forward(500)
    ammu.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
