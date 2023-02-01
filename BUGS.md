# Bugs found in the wild

## Game

1. [OPEN] When my guess contains 2 or more of the same letter, but the right word only has one of that letter, the UI returns yellow for the letter in the wrong place(s). 
    * ex: Right word is SANER, but guess is SURER:  R in the third position is yellow.  
    * In this example, R in the 5th position is correct.  Therefore, R in the third position should not be colorized. 
    * Make sure that you don't silence letters that should be colorized as in the example where my guess is TENSE or STEER, and the answer is ESTER.  Both Es should be colorized.

1. [OPEN] Not used letters should not be repeated in the list. 
    * ex: The word is SPINE, and my first guess is CRIMP.  Then my next guess is MIMES. 
        * In the above example, "Not letters" should not have more than one M in the list returned in the second guess. 
    * Perhaps find a better way of indicating the not used letters in the UI. 

1. [OPEN] Accept more than just the approved matchable words.  If word is in global_list, but not in match_list, still accept the guess. 

## Find_word

2. [IN PROGRESS] Suggest a word to choose next? 
    * [CLOSED] Start off by choosing a random word from the list. 
    * [OPEN] Could implement a calculation of greatest entropy later.
