print("Welcome to the Ultimate Roller Coaster Checker 2023 Edition!")
height = int(input("Enter your height in cm: "))

bill = 0
photo_price = 3

if height >= 120:
    age = int(input("Enter your age in earth years: "))
    if age < 12:
        bill += 5
        print(f"You can ride!\n"
              f"The child ticket is U${bill},00.")
    elif age <= 18:
        bill += 7
        print(f"You can ride!\n"
              f"The youth ticket is U${bill},00.")
    elif 45 < age < 55:
        midlife_crisis = input("Are you having a midlife crisis? Y or N: ")
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
