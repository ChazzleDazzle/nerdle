#!/usr/bin/env python3

import re

import colorama
from colorama import Fore, Back, Style

from find_word import find_words
from models import WordleGame

colorama.init()


def main():
    wordle = WordleGame()
    game_over = False
    word_params = {"not_letters": [], "any_letters": []}
    guesses = 0
    while not game_over:
        guess = validate_guess(wordle.word_list, input("please guess a word: "))
        if not guess:

            continue
        response = wordle.make_guess(guess)
        guesses += 1
        if isinstance(response, str):
            print(response)
            print(f"Number of guesses: {guesses}")
            game_over = True
            continue
        print(
            f"{colorize_letter(response[0])} {colorize_letter(response[1])} {colorize_letter(response[2])} {colorize_letter(response[3])} {colorize_letter(response[4])}"
        )
        for l in response:
            if not l.get("is_used"):
                word_params["not_letters"].append(l.get("letter"))
            else:
                if l.get("is_pos"):
                    position = guess.find(l.get("letter")) + 1
                    word_params[f"l{position}"] = l.get("letter")
                else:
                    word_params["any_letters"].append(l.get("letter"))
        print(f"Not used: {word_params.get('not_letters')}")
        # print(find_words(**word_params))


def colorize_letter(l: dict) -> str:
    if l.get("is_used") and l.get("is_pos"):
        return f"{Fore.BLACK}{Back.GREEN}{l.get('letter').upper()}{Style.RESET_ALL}"
    if l.get("is_used"):
        return f"{Fore.BLACK}{Back.YELLOW}{l.get('letter').upper()}{Style.RESET_ALL}"
    return f"{l.get('letter').upper()}"


def validate_guess(word_list, guess):
    p = re.compile("^[a-zA-Z]{5}$")
    if p.search(guess):
        if guess in word_list:
            return guess.lower()
        else:
            print(f"{guess} is not in the word list")
    else:
        print("Try again using only 5 letters.")


if __name__ == "__main__":
    main()
