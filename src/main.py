#!/usr/bin/env python3

import re

import colorama
from colorama import Fore, Back, Style

from models import WordleGame

colorama.init()


def main():
    wordle = WordleGame()
    max_guesses = 6

    word_params = {"not_letters": [], "any_letters": []}
    while not wordle.game_over:
        if len(wordle.guesses) < max_guesses:
            guess = validate_guess(wordle.word_list, input("Enter your guess: ").lower())
            if not guess:
                continue
            wordle.guesses.append(guess)
            response = wordle.make_guess(guess)
            if isinstance(response, str):
                print(response)
                wordle.game_over = True
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
            print(f"{max_guesses - len(wordle.guesses)} guesses remaining...")
            print(f"Not used: {set(word_params.get('not_letters'))}")
        else:
            wordle.game_over = True
            print(wordle.fail_response())



def colorize_letter(l: dict) -> str:
    if l.get("is_used") and l.get("is_pos"):
        return f"{Fore.BLACK}{Back.GREEN}{l.get('letter').upper()}{Style.RESET_ALL}"
    if l.get("is_used"):
        return f"{Fore.BLACK}{Back.YELLOW}{l.get('letter').upper()}{Style.RESET_ALL}"
    return f"{l.get('letter').upper()}"


def validate_guess(word_list, guess):
    # Guesses are 5 characters long, containing only letters a-z, case insensitive.
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
