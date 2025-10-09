import random

from random_words import easy_word_list, medium_word_list, hard_word_list
from hang_man import stages

DIFFICULTY_LEVEL = "medium"

def hangman(tries):
    return stages[tries]

def get_word():
    if DIFFICULTY_LEVEL == "ease":
        word = random.choice(easy_word_list)
    elif DIFFICULTY_LEVEL == "medium":
        word = random.choice(medium_word_list)
    elif DIFFICULTY_LEVEL == "hard":
        word = random.choice(hard_word_list)
    else:
        word = random.choice(medium_word_list)
    return word.upper()

def choose_difficulty():
    global DIFFICULTY_LEVEL

    DIFFICULTY_LEVEL = input("Choose difficulty level (easy, medium, hard): ").lower()

    if DIFFICULTY_LEVEL == "ease": 
        return 8
    elif DIFFICULTY_LEVEL == "medium":
        return 6
    elif DIFFICULTY_LEVEL == "hard":
        return 4
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        return 6
    
def play(word, initial_tries):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guesses_words = []

    tries = initial_tries

    print("\n-----------Welcome to Hangman-----------")
    print(hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Guess the word:- ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, " is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job, ", guess, " is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)

                indices = [i for i, letter in enumerate(word) if letter == guess]
                
                for index in indices:
                    word_as_list[index] = guess
                    
                word_completion = "".join(word_as_list)

                if "_" not in word-word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guesses_words:
                print("You already guessed the word ", guess)
            elif guess != word:
                print(guess, " is not the word")
                tries -= 1
                guesses_words.append(guess)

            else:
                guessed = True
                word_completion = word
        else:
            print("An incorrect guess.")
        print(hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". play again :)")

def main():
    difficulty = choose_difficulty()
    word = get_word()
    play(word, difficulty)
    
    while input("Do you want to play hangman? (y/n): ").upper() == "Y":
        difficulty = choose_difficulty()
        word = get_word()
        play(word, difficulty)

if __name__ == "__main__":
    main()


    

