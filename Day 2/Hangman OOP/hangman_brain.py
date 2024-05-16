# Object-Oriented Programming (OOP) is a programming paradigm that expands and modulates the way we approach code.
# Instead of thinking about the code as a bunch of functions, attributes and pricedures, we think about entire objects
# and their characteristics.

# An Object is an entity that has both attributes(characteristics) and methods(functions). They're declared in a class
# that will contain all their characteristics and that, through imports, can be used in different programs.

# What happens then is that we create an Object with fixed attributes and methods instead of recreating them everytime.
# Each use o these objects is what we call an instance.
import random


class HangmanBrain:

    def __init__(self, win_art, stages_art, logo_art):
        self.chosen_word = ''
        self.chosen_word_list = [char for char in self.chosen_word]
        self.hidden_word = []
        self.win_art = win_art
        self.stages_art = stages_art
        self.logo_art = logo_art
        self.chances = 6
        self.guesses = []
        self.chosen_topic = ''

    def define_word(self, source):
        chosen_group = random.choice(source)
        self.chosen_topic = chosen_group['theme']
        self.chosen_word = random.choice(chosen_group['words'])
        for character in self.chosen_word:
            self.hidden_word.append("_")

    def change_hidden_word(self, user_guess):
        for index, character in enumerate(self.chosen_word):
            if user_guess == character:
                self.hidden_word[index] = character

    def check_letter_guess(self, user_guess):
        if user_guess in self.chosen_word:
            print("Right Guess")
            return True
        else:
            print("Wrong Guess")
            return False

    def check_whole_guess(self, user_guess):
        if user_guess.lower() == self.chosen_word.lower():
            print("Right Guess")
            for index, character in enumerate(self.chosen_word):
                self.hidden_word[index] = character
            return True
        else:
            print("Wrong Guess")
            return False

    def display_state(self, guess_is_right):
        if guess_is_right:
            print(self.stages_art[self.chances])
            print(''.join(self.hidden_word))
        else:
            self.chances -= 1
            print(self.stages_art[self.chances])
            print(''.join(self.hidden_word))

    def game_over_check(self):
        if "_" not in self.hidden_word:
            print(self.win_art)
            print("Parabéns, você o salvou! Se bem que... por que ele estava preso, afinal? E se ele fosse um assassino"
                  " em série?!")
        else:
            print("Você deixou ele morrer, biruta! O que você tem de errado?!")
