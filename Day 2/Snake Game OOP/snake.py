from turtle import Turtle


class Snake:
    def __init__(self):
        self.x_axis = 0
        self.snake = self.create_snake()
        self.east = 0
        self.north = 90
        self.west = 180
        self.south = 270

    def create_snake(self):
        snake = []

        for _ in range(3):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            segment.width(20)
            segment.setposition(x=self.x_axis, y=0)
            self.x_axis -= 20

            snake.append(segment)

        return snake

    def add_segment(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.width(20)
        segment.setposition(x=self.snake[-1].xcor(), y=self.snake[-1].ycor())

        self.snake.append(segment)

    def move(self):
        for index in range(len(self.snake)-1, 0, -1):
            self.snake[index].setposition(self.snake[index-1].xcor(), self.snake[index-1].ycor())

        self.snake[0].forward(20)

    def turn_left(self):
        if self.snake[0].heading() == self.south or self.snake[0].heading() == self.north:
            self.snake[0].setheading(self.west)

    def turn_right(self):
        if self.snake[0].heading() == self.south or self.snake[0].heading() == self.north:
            self.snake[0].setheading(self.east)

    def turn_up(self):
        if self.snake[0].heading() == self.west or self.snake[0].heading() == self.east:
            self.snake[0].setheading(self.north)

    def turn_down(self):
        if self.snake[0].heading() == self.west or self.snake[0].heading() == self.east:
            self.snake[0].setheading(self.south)
