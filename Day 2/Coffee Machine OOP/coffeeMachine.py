# No, in OOP, things can be more modular through the use of both classes and functions. No let's get to each step.

# TODO: Declare the class
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "água": 300,
            "leite": 200,
            "café": 100,
        }

# TODO: Function that prints the report of the resources
    def report(self):
        """Prints a report of all resources."""
        print(f"Água: {self.resources['água']}ml")
        print(f"Leite: {self.resources['leite']}ml")
        print(f"Café: {self.resources['café']}g")

# TODO: Function that calculates if brewing is possible and then deducts resources and adds to the bill
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sinto muito, não há {item} o suficiente.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui está o seu {order.name} ☕️. Aproveite e volte sempre!")



