# This project was a great way to understand the logic behind OOP and to practice it.
# Firstly, the imports as we can see in the following lines.
# Importing individual modules like the first four is interesting to improve the program's performance by decreasing
# the amount of content it has to import from other modules.

from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

# Here I created an instance of the Screen class and, by understanding some of its main functions from the module's
# documentation, I created the basic screen setup for the Snake game.
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)
my_screen.listen()

# Here I created the instances for everything my game will have: the scoreboard, the "food" and the snake itself.
# An interesting aspect of both the food and the scoreboard regarding inheritance will be discussed inside
# the food's module. For now we only have to understand that his is how we create an object, or instance, from a class.
snake = Snake()
scoreboard = Scoreboard()
food = Food()
food.create_food()

# Simple while loop that'll keep everything in the game working so long as no game over condition has been met,
# i.e the snake hits the "walls" or it's own body.
game_is_on = True
while game_is_on:
    # This "update" function is an interesting feature from the Screen class, and it's worth explaining.
    # Because of the snake's actions, the food's placement and also the score, the screen must keep on 'refreshing'
    # from time to time, just like what happens in any other video game. In order to do that, this function works
    # alongside the 'tracer' function(line 18), which is responsible for freezing the screen until it is instructed to
    # update again(hence the name of the function below).

    my_screen.update()
    # The time widow the program waits before updating is controlled by this function, which in turn comes from another
    # import(from the "time" method, line 10)
    sleep(0.1)

    # Here is another situation where we work with class functions. The "snake" object is using the "move" function
    # to start the snake's movement. The logic that composes the function is written inside the 'snake' module.
    snake.move()
    # This, in turn, use a function from the "screen" class(onkey) that works in pair with another
    # function(listen, line 19) to make something happen in the program when a certain key is pressed.
    # It lets the developer chose what happens and when with the use of parameters.
    my_screen.onkey(fun=snake.turn_left, key="Left")
    my_screen.onkey(fun=snake.turn_right, key="Right")
    my_screen.onkey(fun=snake.turn_up, key="Up")
    my_screen.onkey(fun=snake.turn_down, key="Down")

    # This is the logic that'll make the game react to when the snake eats the food that was randomly generated on
    # the screen. If this happens, the current food is deleted and another one is randomly created somewhere else.
    # Also, the score changes and the snake's size increases.
    if snake.snake[0].distance(food) < 16:
        scoreboard.change_score()
        snake.add_segment()
        food.create_food()

    # This is the game over logic. Whenever the head of the snake gets too close, I.e hits, either itself or
    # the limits of the game's screen, the game over screen is displayed and the loop stops.
    for segment in snake.snake[1:]:
        if (snake.snake[0].distance(segment) < 2 or snake.snake[0].xcor() > 299 or snake.snake[0].xcor() < -299 or
                snake.snake[0].ycor() > 299 or snake.snake[0].ycor() < -299):
            scoreboard.game_over()
            game_is_on = False

# This function simply ensures that the screen window will only close after the user/developer clicks somewhere on it.
my_screen.exitonclick()
