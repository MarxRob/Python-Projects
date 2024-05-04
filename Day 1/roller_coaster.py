# Initial print that presents the program and first input that'll dictate the program's procedure
print("Welcome to the Ultimate Roller Coaster Checker 2023 Edition!")

while True:
    try:
        height = int(input("Enter your height in cm: "))
        break
    except ValueError:
        print("Please, enter your height in numbers.")

# Variables related to prices are declared
bill = 0
age = 0
midlife_crisis = ''
photo_price = 3

# If/else that returns either the final bill or a warning saying that the user isn't tall enough
if height >= 120:
    # While loops as this one, along side with try/except blocks will be used to prevent the user from inserting
    # wrong answers and ending up breaking the program
    while True:
        try:
            age = int(input("Enter your age in earth years: "))
            break
        except ValueError:
            print("Please, enter your age in numbers.")
            continue
    if age < 12:
        bill += 5
        print(f"You can ride!\n"
              f"The child ticket is U${bill},00.")
    elif age <= 18:
        bill += 7
        print(f"You can ride!\n"
              f"The youth ticket is U${bill},00.")
    elif 45 < age < 55:
        while True:
            try:
                midlife_crisis = input("Are you having a midlife crisis? Y or N: ").upper()
                break
            except ValueError:
                print("Please, enter a valid answer")
                continue
        if midlife_crisis == "Y":
            print("Everything's gonna be fine, my friend. Have a ride on the house❤️!")
        else:
            bill += 12
            print("Oof, thank god!")
    else:
        bill += 12
        print(f"You can ride!\n"
              f"The adult ticket is U${bill},00.")

    photos = input("Do you want to have photos of your ride for only U$3,00? Y or N: ").upper()
    if photos == "Y":
        print(f"Your total bill is U${bill + photo_price},00. Enjoy your ride!")
    else:
        print(f"Your total bill is U${bill},00. Enjoy your ride!")
else:
    print("Sorry, you're not tall enough.")
