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

1. [CLOSED] I should be able to indicate that a letter is "Any letter, but not X position". 
    * ex: The word is SHRUG, and I guess CRIMP.  I get back that R is a letter, but does not go in the second position. 
    * In the above example, I should be able to indicate that R is any letter except l2. 
    * Maybe an -nl[12345] flag?

1. [CLOSED] any_letter means that the word must contain that letter.
    * ex: currently, if I supply the tool with `-a asrb`, I get words like "union".

1. [IN_PROGRESS] Suggest a word to choose next? 
    * [CLOSED] Start off by choosing a random word from the list. 
    * [OPEN] Could implement a calculation of greatest entropy later. 

1. [OPEN] Indicate that a letter is not repeated.  
    * ex: The word is GROIN, and I guess BROOK.
        * In the example above, the user should be able to indicate that the second O is not repeated in position 4, or anywhere else. 
    * ex: The word is ABACK, and I guess APNEA. 
        * In the example above, the user should be able to indicate that the second A is used somewhere, but not in this position.

