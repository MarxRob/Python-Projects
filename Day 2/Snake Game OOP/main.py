from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()

snake = Snake()
scoreboard = Scoreboard()
food = Food()
food.create_food()

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()
    my_screen.onkey(fun=snake.turn_left, key="Left")
    my_screen.onkey(fun=snake.turn_right, key="Right")
    my_screen.onkey(fun=snake.turn_up, key="Up")
    my_screen.onkey(fun=snake.turn_down, key="Down")

    if snake.snake[0].distance(food) < 16:
        scoreboard.change_score()
        snake.add_segment()
        food.create_food()

    for segment in snake.snake[1:]:
        if (snake.snake[0].distance(segment) < 2 or snake.snake[0].xcor() > 299 or snake.snake[0].xcor() < -299 or
                snake.snake[0].ycor() > 299 or snake.snake[0].ycor() < -299):
            scoreboard.game_over()
            game_is_on = False


my_screen.exitonclick()
