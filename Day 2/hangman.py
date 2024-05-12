# This program was supposed to mimic a very famous game, The Hangman. And with all its variables, functions and loops,
# it actually does its job, but maybe not in the bast way possible.

# With a quick look, one can see how cluttered this code is. Even with several comments and function explanations,
# this way of programming (commonly called procedural programing) isn't neither scalable nor visually friendly.

# With this much code, things could get messy really fast, so maybe we should consider another approach. Maybe we could
# work with a new programming paradigm.

# And this is where Object-Oriented Programming(OOP) kicks in.

# (This version also lacks some robustness when it comes to possible errors that can surface when the user inserts
# unexpected inputs. This will also be addressed in the new version.)

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
saved = '''
                     ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
'''
logo_hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

# TODO: Declare variable that'll hold the words(Probably a dictionary?)
WORDS_LIST = [
    {
        "theme": "Modelo de carro brasileiro",
        "words": ["Gol", "Onix", "Argo", "Corolla", "Saveiro", "Palio", "Kwid", "Voyage", "Siena", "Punto"]
    },
    {
        "theme": "Rapper estadunidense",
        "words": ["Eminem", "Kendrick Lamar", "Chris Brown", "Kanye West", "Future", "Travis Scott"]
    },
    {
        "theme": "Filme de Martin Scorsese",
        "words": ["Goodfellas", "Taxi Driver", "The Departed", "Shutter Island", "Wolf of Wallstreet"]
    }
]

# TODO: Declare both the variable that'll hold the chosen word + the one who will mimic it with empty spaces
chances = len(stages) - 1
guesses = []
word_group = random.choice(WORDS_LIST)
chosen_theme = word_group["theme"]
user_letter = ""
chosen_word = random.choice(word_group["words"]).lower()
hidden_word_list = []
for i in chosen_word:
    if i == " ":
        hidden_word_list.append(" ")
    else:
        hidden_word_list.append("_")
hidden_word = ""


def hidden_word_creator():
    global hidden_word

    hidden_word = "".join(hidden_word_list)


hidden_word_creator()
# TODO: Show UI + hidden word with tip an ask for the user's letter
print(logo_hangman)
print("Bem-vindo(a) ao jogo da forca!")


def saved_display():
    """Displays the saved screen when the user wins"""

    global chances

    print(f"Parabéns, você ganhou o jogo e salvou o camarada da forca :D\n"
          f"{saved}")
    chances = 0


def display_ui():
    """Displays User Interface based on the game state. If user won, the saved display is showed through its respective
     function. If the user lost, the same happens with the game over display. If the game is not over yet, then it just
     keeps displaying the current state."""

    global user_letter

    if "_" not in hidden_word:
        saved_display()
    elif chances == 0:
        print(stages[chances])
        print(f"Ah, não! Você deixou ele falecer!! Quanta falta de empatia!!!\n"
              f"Aliás, a palavra era {chosen_word}.")
    else:
        print(stages[chances])
        print(hidden_word)
        print(f"A dica para essa palavra é: {chosen_theme}")
        user_letter = input("Escolha uma letra, ou chute a palavra digitando '0': ").lower()

# TODO: Create logic that'll check whether the user was right in their guess and act accordingly


def guess_check():
    """Evaluates the user guess based on the user input. If it's a letter, then the program will check whether that
    letter is inside the chosen word. if it's a '0', then the user will be prompted to guess the entire word."""

    global hidden_word_list, chances
    is_there = 0

    if user_letter == "0":
        guessed_word = input("Qual será o seu chute?: ").lower()
        if guessed_word == chosen_word:
            saved_display()
        else:
            print("Você errou!")
            display_ui()
    else:
        if user_letter in guesses:
            print("Você já tentou essa letra!")
        else:
            for index, letter in enumerate(chosen_word):
                if letter == user_letter:
                    is_there += 1
                    hidden_word_list[index] = letter

                if letter not in chosen_word:
                    chances -= 1

    hidden_word_creator()
    guesses.append(user_letter)


def play_game():
    """Starts the game in a loop and asks the user whether they want to play again when the game is over."""

    while True:
        while chances:
            # print(chosen_word)
            display_ui()
            # print(guesses)
            guess_check()
        replay = input("Quer jogar novamente?(S/N): ").lower()
        if replay == "y":
            continue
        else:
            break


play_game()
