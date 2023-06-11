
import random
from words import word_list
import platform
import os

if platform.system() == "Windows":
    def clear_scr():
        os.system("cls")
else:
    def clear_scr():
        os.system("clear")

def random_word():
    word = random.choice(word_list)
    return word

word = random_word()


def play (word):
    clear_scr()
    wrong_ans = 0
    guessed_letters = []
    guessed = False
    word_completion = "-" * len(word)
    print(word_completion)
    while wrong_ans < 5 and not guessed:
        if wrong_ans == 0 :
            print ("________\n|      |\n|      O\n|       \n|       \n|_______")
        if wrong_ans == 1 :
            print ("________\n|      |\n|      O\n|      |\n|       \n|_______")
        if wrong_ans == 2 :
            print ("________\n|      |\n|      O\n|     /|\n|       \n|_______")
        if wrong_ans == 3 :
            print ("________\n|      |\n|      O\n|     /|\ \n|       \n|_______")
        if wrong_ans == 4 :
            print ("________\n|      |\n|      O\n|     /|\ \n|     /\n|_______")
        guess = input("\nguess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear_scr()
                print("You already guessed the letter", guess)
                print("wrong guesses: ", wrong_ans)
            elif guess not in word:
                clear_scr()
                print(guess, "is not in the word.")
                wrong_ans += 1
                print("wrong guesses: ", wrong_ans)
                guessed_letters.append(guess)
            else:
                clear_scr()
                print( guess, "is in the word!")
                print("wrong guesses: ", wrong_ans)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "-" not in word_completion:
                    guessed = True
        else:
            print("Not a valid guess.")
        print(word_completion)
    if guessed:
        print("You win!")
        user_choice3 = input("""select an option:
1)back to menu
2)Exit

1-2: """)
    else:
        clear_scr()
        print ("\n________\n|      |\n|      O\n|     /|\ \n|     / \ \n|_______")
        print ("\nGAME OVER")
        print("You ran out of tries. The word was (" + word + ").")
        user_choice3 = input("""select an option:
1)Back to menu
2)Exit
1-2: """)
    return user_choice3  


def menu():
    re_match = 0
    while True:
        clear_scr()
        print("""select an option:
1)Help
2)Play Hangman
3)Exit""")
        users_choice1 = input("1-3: ")
        if users_choice1 == "1":
            clear_scr()
            print("user guide ...")
            print("""select an option:
1)Play Hangman
2)Exit""")
            users_choice2 = input("1-2: ")
            if users_choice2 == "1" :
                re_match = play(word)
                return re_match
            else:
                break
        if users_choice1 == "2":
            re_match = play(word)
            return re_match
        else:
            break        

re_match = 0


while True:
    word = random_word()
    re_match = menu()
    if re_match != "1":
        break