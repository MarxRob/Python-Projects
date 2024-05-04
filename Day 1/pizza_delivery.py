print("Welcome to The Ultimate Python Pizza Deliveries 2023!\n"
      "The prices according to sizes are:\n"
      "Large: U$25,00\n"
      "Medium: U$20,00\n"
      "Small: U$15,00")

# When I get the user input. Here is an interesting place. I could come up with a bug because, say, the user might
# enter a number instead of a string. And this can cause a bug. BUT! I can always use a while loop to fix it.

while True:
    # This is also a good opportunity to use 'try/except' code blocks. In this case, the computer will try to get the
    # input from the user but if it isn't anything inside the list, then an error is raised as 'ValueError' with its
    # respective message.
    try:
        size = input("Enter which size of pizza do you want (L, M, S): ").upper()
        if size not in ["L", "M", "S"]:
            raise ValueError("Invalid choice. Please enter 'L' for Large, 'M' for Medium, or 'S' for Small.")
        break  # If a valid size is entered, the loop breaks
    except ValueError as e:
        # This is a way to call for the error message in the exception case of the raised error. Then the loop starts
        # over again.
        print(e)

bill = 0
# Here a dictionary containing the prices in relation to the pizza sizes is declared
prices_dict = {
    "L": [25, 3, 1],
    "M": [20, 3, 1],
    "S": [15, 2, 1]
    }
add_pepperoni = ""
extra_cheese = ""


def define_bill(user_input):
    """Asks whether user wants pepperoni and/or cheese and then, based on the user's input regarding the pizza size,
    the final bill is calculated and printed."""

    global add_pepperoni, extra_cheese, bill

    # This is a clever way to increment the current price to the bill using whatever the user entered to locate
    # the proper price in the price dictionary
    bill += prices_dict[user_input][0]
    while add_pepperoni not in ["Y", "N"]:
        add_pepperoni = input("Do you want pepperoni for U$3,00? Y or N: ").upper()
        if add_pepperoni not in ["Y", "N"]:
            print("Please, enter only 'Y' for Yes or 'N' for No.")
    if add_pepperoni == "Y":
        bill += prices_dict[user_input][1]

    while extra_cheese not in ["Y", "N"]:
        extra_cheese = input("Do you want extra cheese for U$1,00? Y or N: ").upper()
        if extra_cheese not in ["Y", "N"]:
            print("Please, enter only 'Y' for Yes or 'N' for No.")
    if extra_cheese == "Y":
        bill += prices_dict[user_input][2]

    print(f"Your final bill is U${bill},00.")


define_bill(size)

# Below is an older code that produces the same result, but with a much bigger amount of code

# if size == "L":
#     bill += 25
#     add_pepperoni = input("Do you want pepperoni for U$3,00? Y or N: ").upper()
#     if add_pepperoni == "Y":
#         bill += 3
#     extra_cheese = input("Do you want extra cheese for U$1,00? Y or N: ").upper()
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is U${bill},00")
# elif size == "M":
#     bill += 20
#     add_pepperoni = input("Do you want pepperoni for only U$3,00? Y or N: ").upper()
#     if add_pepperoni == "Y":
#         bill += 3
#     extra_cheese = input("Do you want extra cheese U$1,00? Y or N: ").upper()
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is U${bill},00")
# elif size == "S":
#     bill += 15
#     add_pepperoni = input("Do you want pepperoni for only U$2,00? Y or N: ").upper()
#     if add_pepperoni == "Y":
#         bill += 2
#     extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
#     if extra_cheese == "Y":
#         bill += 1
#     print(f"Your final bill is U${bill},00")
