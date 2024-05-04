# Basic program presentation with print statement
print("Welcome to the Ultimate Compatibility Test 2023 Edition!❤️❤️")
# Just getting the important data from the user via inputs
your_name = input("Enter your name🫵: ").lower()
their_name = input("Enter the name of your lover🥵: ").lower()

# Constant variables being declared
WORD_TRUE = "true"
WORD_LOVE = "love"
both_names = your_name + their_name
letter_count = 0

# Loop that iterates through each word and, if the letter is in either of the words, the count will be incremented
for char in both_names:
    if (char in WORD_TRUE) or (char in WORD_LOVE):
        letter_count += 1

# If/else block that decides what shall be printed depending on the score of the 'letter_count' variable
if 10 < letter_count or letter_count > 90:
    print(f"Your score is {letter_count}, you go together like coke and mentos🌋💥.")
elif 40 < letter_count < 50:
    print(f"Your score is *{letter_count}, you are alright together☕❣️.")
else:
    print(f"Your score is {letter_count}.")
