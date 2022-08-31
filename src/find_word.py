#!/usr/bin/env python3

import argparse
from random import randint

from words import WordList


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l1", help="Letter number 1.")
    parser.add_argument("-l2", help="Letter number 2.")
    parser.add_argument("-l3", help="Letter number 3.")
    parser.add_argument("-l4", help="Letter number 4.")
    parser.add_argument("-l5", help="Letter number 5.")
    parser.add_argument("-n", "--not-letters", help="All letters that can be excluded.")
    parser.add_argument(
        "-nl1",
        help="All letters that are not letter 1.",
    )
    parser.add_argument(
        "-nl2",
        help="All letters that are not letter 2.",
    )
    parser.add_argument(
        "-nl3",
        help="All letters that are not letter 3.",
    )
    parser.add_argument(
        "-nl4",
        help="All letters that are not letter 4.",
    )
    parser.add_argument(
        "-nl5",
        help="All letters that are not letter 5.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action='store_true',
        help="Show extra information."
    )

    args = parser.parse_args()
    response = find_words(
        l1=args.l1,
        l2=args.l2,
        l3=args.l3,
        l4=args.l4,
        l5=args.l5,
        not_letters=args.not_letters,
        nl1=args.nl1,
        nl2=args.nl2,
        nl3=args.nl3,
        nl4=args.nl4,
        nl5=args.nl5,
    )
    if args.verbose:
        print(response)
    print(f"\nPossible words: {len(response)}")
    print(f"Try the word: {response[randint(0, len(response) - 1)].upper()}")


def find_words(
    l1=None,
    l2=None,
    l3=None,
    l4=None,
    l5=None,
    not_letters=[],
    nl1=[],
    nl2=[],
    nl3=[],
    nl4=[],
    nl5=[],
):

    any_letters = add_not_position_to_any_letters(nl1, nl2, nl3, nl4, nl5)
    word_list = WordList().match_list
    word_list = filter_locked_letters(word_list, l1, l2, l3, l4, l5)
    word_list = filter_not_position(word_list, nl1, nl2, nl3, nl4, nl5)
    if not_letters:
        word_list = list(
            set(
                [
                    word
                    for word in word_list
                    if not set(not_letters).intersection(set(word))
                ]
            )
        )
    if any_letters:
        word_list = list(
            set([word for word in word_list if set(any_letters).issubset(set(word))])
        )

    return sorted(word_list)


def _filter_locked_letter(word_list, locked_letter, position):
    return [word for word in word_list if word[position] == locked_letter]


def filter_locked_letters(word_list, l1, l2, l3, l4, l5):
    if l1:
        word_list = _filter_locked_letter(word_list, l1, 0)
    if l2:
        word_list = _filter_locked_letter(word_list, l2, 1)
    if l3:
        word_list = _filter_locked_letter(word_list, l3, 2)
    if l4:
        word_list = _filter_locked_letter(word_list, l4, 3)
    if l5:
        word_list = _filter_locked_letter(word_list, l5, 4)
    return word_list


def _filter_not_this_position(word_list, letter, position):
    return [word for word in word_list if not word[position] == letter]


def filter_not_position(word_list, nl1, nl2, nl3, nl4, nl5):
    if nl1:
        for l in nl1:
            word_list = _filter_not_this_position(word_list, l, 0)
    if nl2:
        for l in nl2:
            word_list = _filter_not_this_position(word_list, l, 1)
    if nl3:
        for l in nl3:
            word_list = _filter_not_this_position(word_list, l, 2)
    if nl4:
        for l in nl4:
            word_list = _filter_not_this_position(word_list, l, 3)
    if nl5:
        for l in nl5:
            word_list = _filter_not_this_position(word_list, l, 4)
    return word_list


def add_not_position_to_any_letters(nl1, nl2, nl3, nl4, nl5):
    not_positions = [p for p in [nl1, nl2, nl3, nl4, nl5] if p is not None]
    return "".join(
        list(
            set(
                [
                    letter
                    for position in not_positions
                    for letter in position
                    if position
                ]
            )
        )
    )


if __name__ == "__main__":
    main()
