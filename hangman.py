# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
                                                                #ALLERT!! Function main is pass now,
                                                                #please uncomment one of coupe strings and comment pass
WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for lets_word in secret_word:
        iter = False
        for lets_lets in letters_guessed:
            if lets_word == lets_lets:
                iter = True
                break
        if iter == False:
            break
    return iter



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for let_word in secret_word:
        let = False
        for let_let in letters_guessed:
            if let_word == let_let:
                guessed_word.append(let_word)
                let = True
                break

        if let == False:
            guessed_word.append("_")

    guessed_word = " ".join(guessed_word)
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    for let in string.ascii_lowercase:
        if let not in letters_guessed:
            available_letters.append(let)

    available_letters = "".join(available_letters)
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    gusses = 6
    warning = 3
    letter_guessed = []
    print("\nWelcome to the game Hangman! \nI am thinking of a word that is ", len(secret_word), " letters long.")

    while True:
        if get_guessed_word(secret_word, letter_guessed).replace(" ", "").isalpha():
            print("YOU WIN!")
            break
        if gusses <= 0:
            print("You lose")
            break

        print(
            "\n--------------\n\nYou have {1} warnings left. \nYou have {0} guesses left. \nAvailable letters: {2} \nPlease guess a letter: ".format(
                gusses, warning, get_available_letters(letter_guessed)))

        try:
            letter = input().lower()
            if not letter.isalpha() or len(letter) != 1:
                warning -= 1
                if warning == 0:
                    warning = 3
                    gusses -= 1

                raise ValueError

            if letter in letter_guessed:
                warning -= 1
                if warning == 0:
                    warning = 3
                    gusses -= 1
                raise Exception

        except ValueError:
            print("Oops! That is not a valid letter. You have {0} warnings left: ".format(warning,
            get_guessed_word(secret_word,letter_guessed)))
            continue

        except Exception:
            print("Oops! You've already guessed that letter. You have {0} warnings left: ".format(warning,
            get_guessed_word(secret_word,letter_guessed)))
            continue

        letter_guessed.append(letter)
        if letter in secret_word:
            print("Good guess: ", get_guessed_word(secret_word, letter_guessed))
        elif letter in "aouie":
            gusses -= 2
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letter_guessed))
        else:
            gusses -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letter_guessed))







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.split()
    if len(my_word) == len(other_word):
        i = 0
        for letter in my_word:
            if letter != "_":
                if letter in other_word and my_word[i] == other_word[i]:
                    pass

                else:
                    return False
                    break

            i += 1

        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    exist = 0
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            print(other_word, end = " ")
            exist += 1

    if exist == 0:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    gusses = 6
    warning = 3
    letter_guessed = []
    print("\nWelcome to the game Hangman! \nI am thinking of a word that is ", len(secret_word), " letters long.")

    while True:
        if get_guessed_word(secret_word, letter_guessed).replace(" ", "").isalpha():
            print("YOU WIN!")
            break
        if gusses <= 0:
            print("You lose")
            break

        print(
            "\n--------------\n\nYou have {1} warnings left. \nYou have {0} guesses left. \nAvailable letters: {2} \nPlease guess a letter: ".format(
                gusses, warning, get_available_letters(letter_guessed)))

        try:
            letter = input().lower()
            if letter == "*":
                show_possible_matches(get_guessed_word(secret_word,letter_guessed))
                continue

            elif not letter.isalpha() or len(letter) != 1:
                warning -= 1
                if warning == 0:
                    warning = 3
                    gusses -= 1

                raise ValueError

            elif letter in letter_guessed:
                warning -= 1
                if warning == 0:
                    warning = 3
                    gusses -= 1
                raise Exception

        except ValueError:
            print("Oops! That is not a valid letter. You have {0} warnings left: ".format(warning,
                                                                                          get_guessed_word(secret_word,
                                                                                                           letter_guessed)))
            continue

        except Exception:
            print("Oops! You've already guessed that letter. You have {0} warnings left: ".format(warning,
                                                                                                  get_guessed_word(
                                                                                                      secret_word,
                                                                                                      letter_guessed)))
            continue

        letter_guessed.append(letter)
        if letter in secret_word:
            print("Good guess: ", get_guessed_word(secret_word, letter_guessed))
        elif letter in "aouie":
            gusses -= 2
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letter_guessed))
        else:
            gusses -= 1
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letter_guessed))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
