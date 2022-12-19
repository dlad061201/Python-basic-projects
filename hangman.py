import random

# choosing a word for game
def random_word():
    word = random.choice(["ironman", "thor", "hulk", "captain america", "black widow", "hawkeye", "spiderman", "captain marvel", "black panther", "groot", "drax", "gamora", "doctor strange"])
    return word.upper()

def game(word):
    # intial values
    complete_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 9

    # user interface
    print("Guess the word: ")
    print(complete_word)
    print(hangman_display(tries))

    #while loop
    while not guessed and tries > 0:
        # user input
        guess = input("Letter: ").upper()

        # 1 - if guess is a letter and an alphabet
        if len(guess) == 1 and guess.isalpha():
            # 1.1 - if you have already guessed that letter
            if guess in guessed_letters:
                print("You've already guessed the letter.")
            # 1.2 - if the guess is incorrect
            elif guess not in word:
                print("The letter is not in the word.")
                # reduce the number of tries
                tries = tries - 1
                # add the letter to the list of guessed letters
                guessed_letters.append(guess)
                print("You have ",tries,"left.")
            # 1.3 - if the guess if correct
            else:
                print("You've guessed the letter correctly.")
                # add the letter to the list of guessed letters
                guessed_letters.append(guess)
                # transform the word into a list
                word_as_list = list(complete_word)
                # in the index of each character of the list, enumerate the coorect guess
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # iterate the list to print
                for index in indices:
                    word_as_list[index] = guess
                # update the complete_word by relacing - with the correct Guess
                complete_word = "".join(word_as_list)
                # see if there is no _, the word is guessed
                if "_" not in complete_word:
                    guessed = True

        # 2 - if guess is a word and alphabets
        elif len(guess) == len(word) and guess.isalpha():
            # 2.1 - if the word is already guessed
            if guess in guessed_words:
                print("You've already guessed the word.")
            # 2.2 - if the wrong is incorrect
            elif guess != word:
                print(guess,"is not the word.")
                tries = tries - 1
                guessed_words.append(guess)
            # 2.3 - if your guess is correct
            else:
                guessed = True
                complete_word = word

        # 3 - if guess is neither a letter / word nor alphabet
        else:
            print("Invalid input!")

        print(hangman_display(tries))
        print(complete_word)
    if guessed:
        print("Congratulation! You win.")
    else:
        print("Sorry you've ran out of tries, better luck next time. The word was", word)

def hangman_display(tries):
    stages = [
    # 0 tries left -
    """
    |------
    |  O_|
    | /|\
    | / \
    -
    """,
    # 1 try left
    """
    |------
    |  O |
    | \|/
    | / \
    """,
    # 2 tries left
    """
    |------
    |  O
    | \|/
    | / \
    """,
    # 3 tries left
    """
    |------
    |  O
    | \|/
    | /
    """,
    # 4 tries left
    """
    |------
    |  O
    | \|
    | /
    """,
    # 5 tries left
    """
    |------
    |  O
    | \|
    |
    """,
    # 6 tries left
    """
    |------
    |  O
    |  |
    |
    """,
    # 7 tries left
    """
    |------
    |  O
    |
    |
    """,
    # 8 tries left
    """
    |------
    |
    |
    |
    """,
    # 9 tries left
    """
    |
    |
    |
    |
    """
    ]
    return stages[tries]

name = input("Enter user's name: ")
print ("Welcome to the game,",name)
print ("------------")
print("Try to guess this word in less than 10 attempts.")
word = random_word()
game(word)
while input("Play again? Y/N").upper() == "Y":
    word = random_word()
    game(word)
