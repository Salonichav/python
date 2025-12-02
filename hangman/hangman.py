import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ["python", "hangman", "pneumonia", "xray", "machine", "learning", "programming", "developer", "challenge", "function", "variable", "iteration", "condition", "syntax", "debugging"]

def get_random_word(word_list):
    """Choose a random word from the list."""
    return random.choice(word_list)

def display_game_state(wrong_guesses, guessed_letters, secret_word):
    print(HANGMANPICS[wrong_guesses])
    print("\nGuessed letters:", " ".join(guessed_letters))

    
    blanks = ""
    for letter in secret_word:
        if letter in guessed_letters:
            blanks += letter + " "
        else:
            blanks += "_ "
    print("\nWord:", blanks)

def hangman():
    secret_word = get_random_word(words)
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = len(HANGMANPICS) - 1

    print(" Welcome to Hangman! ")
    print("Try to guess the word.\n")

    while True:
        display_game_state(wrong_guesses, guessed_letters, secret_word)

        guess = input("\nEnter a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(" You already guessed that letter!")
            continue

        guessed_letters.append(guess)

       
        if guess not in secret_word:
            wrong_guesses += 1
            print(" Wrong guess!")
            if wrong_guesses == max_guesses:
                print(HANGMANPICS[wrong_guesses])
                print("\n💀 You lost! The word was:", secret_word)
                break
        else:
            print(" Good guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\n Congratulations! You guessed the word:", secret_word)
            break


hangman()



