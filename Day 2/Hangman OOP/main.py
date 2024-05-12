import data, arts, hangmanBrain


def play_game():
    wants_to_play = True

    while wants_to_play:
        hangman = hangmanBrain.HangmanBrain(
            win_art=arts.saved, stages_art=arts.stages, logo_art=arts.logo_hangman
        )

        hangman.define_word(data.WORDS_LIST)

        print(hangman.logo_art)
        print(hangman.stages_art[hangman.chances])
        print(f"A dica é: {hangman.chosen_topic}")
        print(''.join(hangman.hidden_word))

        game_over = False
        while not game_over:
            user_guess = input("Chute a palavra escrevendo '0', ou tente uma letra: ")
            if user_guess == "0":
                word_guess = input("Qual é a palavra?: ").lower()
                result = hangman.check_whole_guess(word_guess)
            else:
                result = hangman.check_letter_guess(user_guess)

            hangman.change_hidden_word(user_guess)
            hangman.display_state(result)

            if hangman.chances == 0 or "_" not in hangman.hidden_word:
                game_over = True

        hangman.game_over_check()
        user_answer = input("Quer jogar novamente?(Y/N): ").lower()
        if user_answer != 'y':
            wants_to_play = False


if __name__ == "__main__":
    play_game()
