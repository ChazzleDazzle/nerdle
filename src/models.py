from math import floor
from random import uniform

from words import WordList


class WordleGame:
    def __init__(self):
        self.word_list = self._set_word_list()
        self.game_word = self._set_game_word()

    def make_guess(self, guess):
        if guess == self.game_word:
            return f"You win!  The word was {self.game_word}!"
        letter_response = [
            {"letter": guess[0], "is_pos": False, "is_used": False},
            {"letter": guess[1], "is_pos": False, "is_used": False},
            {"letter": guess[2], "is_pos": False, "is_used": False},
            {"letter": guess[3], "is_pos": False, "is_used": False},
            {"letter": guess[4], "is_pos": False, "is_used": False},
        ]
        for idx, letter in enumerate(guess):
            if letter in self.game_word:
                letter_response[idx]["is_used"] = True
                if self.game_word[idx] == guess[idx]:
                    letter_response[idx]["is_pos"] = True
        return letter_response

    def _set_word_list(self):
        return WordList().match_list

    def _set_game_word(self):
        return self.word_list[floor(uniform(0, len(self.word_list)))]
