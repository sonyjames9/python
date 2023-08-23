from turtle import Screen

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# screen.tracer(0)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  screen.update()
  snake.move()

  # Detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # Detect collision with wall
  if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_on = False
    scoreboard.game_over()

  # Detect collision with snake tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      # if head collides with any segment in tail, game over
      game_on = False
      scoreboard.game_over()


screen.exitonclick()
