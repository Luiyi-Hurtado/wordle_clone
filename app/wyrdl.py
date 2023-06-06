#!/usr/bin/env python
"""
prototype for the project
"""

word = "SNAKE"

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num} time: ").upper()
    # the correct word statement
    if guess == word:
        print(f'{guess} is correct')
        break
    # the correct letter
    correct_letters = {letter for letter, correct in zip(
        guess, word) if letter == correct}
    # the misplace letter
    misplaced_letters = set(guess) & set(word) - correct_letters
    # the wrong letter
    wrong_letter = set(guess) - set(word)
    # game feedback
    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ",".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letter)))
