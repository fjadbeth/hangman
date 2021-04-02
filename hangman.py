import random
from hangman_art import stages, logo
from hangman_words import wordList
import os

print(logo)
endOfGame = False
chosenWord = random.choice(wordList)

lives = 6

display = []
for _ in range(len(chosenWord)):
    display += "_"

while not endOfGame:
    guess = input("Guess a letter: ").lower()

    os.system("clear")

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(len(chosenWord)):
        if guess == chosenWord[position]:
            display[position] = chosenWord[position]
    print(f"{' '.join(display)}")
    
    if guess not in chosenWord:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose.")
    
    if "_" not in display:
        endOfGame = True
        print("You win.")

    print(stages[lives])