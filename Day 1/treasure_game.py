print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("The leads you studied for months got you in front of a bifurcation. Do you want to go to the left or to the right?: ").lower()
if "right" in choice_1:
    print("Hell nah, friend. You literally stepped into a black hole! You've been spaghettified and then died immediately. ")
elif "left" in choice_1:
    choice_2 = input("You walked a lot and finally reached a lake. There's a boat slowly drifting your way, coming from a faraway island. Do you want to "
                     "swim "
                     "or wait?: ").lower()
    if "swim" in choice_2:
        print("You feel a slimy touch on your feet. Fear grabs your soul. You're suddenly pulled to the depths of the lake... and never comes back.")
    elif "wait" in choice_2:
        choice_3 = input("Your patience was rewarded. You ride the boat to the island and find a probably haunted mansion. This one is quite "
                         "peculiar, though: there's two big doors at the entrance. Do you enter the white one or the purple one?: ").lower()
        if "white" in choice_3:
            print("What the actual fuck?! You ran into Fabio naked!! Your mind crumbled and you're now in an unending catatonic state(you starved "
                  "afterwards)")
        elif "purple" in choice_3:
            print("You found the treasure chest! You opened it and, inside, there was a picture of Beetle Juice and a Manuel Gomes soundtrack disc.")
