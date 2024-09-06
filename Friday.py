"""Exercise: "Letter Frequency Detective"
Objective:  guess a mystery word based on the frequency of its letters. You'll have three attempts to guess the word correctly.
Instructions:
The program will analyze a randomly chosen word and show you how many times each letter appears.
Based on this letter frequency, try to guess the word.
You have three attempts to guess the word correctly.
Hints:
Pay attention to letters that appear multiple times; they can give you clues about the word.
Think about common words and how their letters are distributed.
If you're stuck, try to think of words that have similar letter patterns to the one shown."""

from collections import Counter
import random
words = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]

def main():
    random_word = random.choice(words)
    latter_count = Counter(random_word)
    print("Welcome to our fruit game")
    print(f"Please guess the fruit, here are the letter accurance,\n{latter_count} ")
    guess_random_word(random_word)


def guess_random_word(random_word):
    attempts = 3
    hints = ["-"]*len(random_word)

    for attempt in range(attempts):
        print(f"Hint: {' '.join(hints)}")
        guess = input(f"Attempt {attempt+1}, guess the fruit")
        if guess == random_word:
            print("You won")
            break
        else:

            print("The fruit is not correct, please try again")
            for i in range(len(random_word)):
                if hints[i] == "-" and random_word[i] == guess[i]:
                    hints[i] = random_word[i]
                    break
                elif hints[i] != "-":
                    break
    print(f"You are out of attempts. The fruit was, {random_word}")


    if guess != random_word:
        print(f"You are out of attempts, the fruit was {random_word}")




if __name__=="__main__":
    main()