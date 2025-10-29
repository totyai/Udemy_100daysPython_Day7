# TODO - Create global variables - create drawing stages lists, Create inputed character list, Create life count, import random
import random
hangman_draw = {"stage6":
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
"stage5": 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
"stage4":
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
"stage3":
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
"stage2":
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
"stage1":'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
"dead":'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}
used_characters = []
life = 6
#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
guess = ""
word = random.choice(words)
word_leng = len(word)
word_len_guessed = 0
placeholder = ""
for i in range(0,word_leng):
    placeholder += "_"
print(word, word_leng)

# TODO - Create End game message, Win message
def end_message():
    if life > 0:
        print(f"Congratulations! You have won, you figured out the word: {word}")
        return
    else:
        print(f"Sorry, you have lost, you have been hanged. The word was: {word}")
        return
        



# TODO - Print number of characters to the screen that is in the choosen word and ask the user for input, input error handling
def guessing():
    global placeholder, guess
    print(f"Your word: {placeholder}")

    guess = input("Enter your guess character: \n")
    while len(guess) != 1:
        guess = input("You need to enter only one character: \n")

    while not guess.isalpha():
        guess = input("Please enter valid character: \n")



# TODO - Validate input, check agenst already given character list
def char_used():
    global guess, used_characters
    while guess in used_characters:
        guess = input("You have already used this character. You can select another: \n")
    used_characters.append(guess)



# TODO - Check if the character is in the word
def char_word_check():
    global guess, word
    if guess in word:
        correct_guess()
    else:
        incorrect_guess()



# TODO - NO, inform user that it is not in, lose life, call in hangman drawing, check life and end game
def incorrect_guess():
    global life, hangman_draw
    life -= 1
    print(f"Your guess is incorrect! You loose a life. Your life remaining: {life}")
    print(f"{hangman_draw[f'stage{life}']}")

  
# TODO - YES, reveale letter's placement, evaluate full guessed, congratulate user, end game
def correct_guess():
    global guess, word, placeholder, word_leng, word_len_guessed
    word_len_guessed += 1
    print("You guessed correctly.")
    # Issue with adding guessed charaters to placeholder
    # Issue with multiple characters in the same word eg. baboon - o
    position = word.index(guess)
    word[position] = guess

# TODO - welcome user, main logic
print(f"Welcome to the game of handman! Below you will need to figure out a random word by guessing characters in it.\n You will see _ _ representing each character in the word. If the character you choice is in the word, it will be releaved, if you miss, one life will be deduced. \n You have {life} lifes in the beginning, if it reaches 0, you lost. Good luck!")
while (word_len_guessed != word_leng) or (life != 0):
    guessing()
    char_used()
    char_word_check()

end_message()