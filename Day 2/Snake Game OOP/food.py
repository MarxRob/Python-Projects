from turtle import Turtle
import random


# Here is an example of how inheritance works. In this case, after inserting class the class "Food" will inherit it's
# initial attributes and functions from, the former will share every single functionality that the latter has.
# That is precisely why this class can make use of functions like "clear"(line 16), even though it wasn't created here.
class Food(Turtle):
    def __init__(self):
        # This "super().__init__()" is where this module's class actually inherits everything from the other class.
        # Inherited traits can be changed. For example, the object's "position" is an attribute that's changed
        # everytime the food is eaten, through the "create_food" function.
        super().__init__()
        self.hideturtle()

    def create_food(self):
        """Deletes the last food eaten and immediately generates another one in a random place"""

        self.clear()
        self.penup()

        self.setposition(random.randint(-200, 200), random.randint(-200, 200))
        self.pendown()
        self.dot(7, "blue")
