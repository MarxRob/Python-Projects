from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def create_food(self):
        self.clear()
        self.penup()

        self.setposition(random.randint(-200, 200), random.randint(-200, 200))
        self.pendown()
        self.dot(7, "blue")
