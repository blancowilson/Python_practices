from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

food = Food()
scoreboard = Scoreboard()
snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

#controllers
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

snake_alive = True
while (snake_alive):
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extends()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
        snake.head.ycor() > 280 or snake.head.ycor() < -280 ):
        scoreboard.check_scores()
        snake.reset()
        food.refresh()
        scoreboard.reset()
        scoreboard.reset_score()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.reset_score()
            snake.reset()

screen.exitonclick()