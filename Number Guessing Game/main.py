# Number Guess Game

import random       # To use random module firstly we should import it
from art import *   # From art.py import everything to main.py
import time         # to use time module firstly we should import it


IS_GAME_ON=True # To create an infinitive loop


def play_again_question():
    global IS_GAME_ON   # We are inside a function because of that if we want to use a variable from outside of fuction we should use this method
    print("\n"*50)
    print(wanna_play_again_logo)
    play_again_question=input("Do you wanna play again? y/n: ").lower()   # Whatever we write is going to be all lowercase
    if play_again_question=="n":
        print("\n"*50)
        print(game_over)
        IS_GAME_ON=False  # To stop loop
    else:
        game()   # To run function
        

def equal():
    print("\n"*50)
    print(correct_logo)
    print( "You guessed the number correct.Congrats")
    time.sleep(3)   # Wait 3 seconds before make other operation
    play_again_question()  # To run function
   

def live_equal_zero():
    print("\n"*50)
    print(wrong_logo)
    print(f"You lost.The number was: {random_number}")
    time.sleep(3)  # Wait 3 seconds before make other operation
    play_again_question()  # To run function



def operations():
    if level=="e":
        lives=10
    else:
        lives=5

    while lives!=0:   # While lives variable not equal to zero
        guess_number=int(input("Guess a number: "))   # Input's default data type is str but I need int data type because of that I converted it
        if guess_number==random_number:
            equal()
        elif guess_number>random_number:
            lives-=1
            print("\nHigh\nguess again\n",f"remaining lives: {lives}\n")
        elif guess_number>random_number+20:
            lives-=1
            print("\n Too High\nguess again\n",f"remaining lives: {lives}\n")
        elif guess_number+20<random_number:
            lives-=1
            print("\nToo Low\nguess again\n",f"remaining lives: {lives}\n")
        elif guess_number<random_number:
                lives-=1
                print("\nLow\nguess again\n",f"remaining lives: {lives}\n")
    if lives==0:
        live_equal_zero()


def game():
    global random_number,level
    while IS_GAME_ON:   # While True
        random_number=random.randint(1,100)   # to choose a random integer number between 1-100
        print("\n"*50)
        print(number_guess_game)
        print("Welcome to the number guess game\nComputer chose a random number between 1-100 try to find it")
        level=input(("Type 'e' to easy level,Type 'h' to hard level: ")).lower()  # Whatever you write is going to be lowercase
        print(random_number)

        if level=="e":
            print("\n"*50) 
            print(easy_logo)  
            print("You have 10 attempts")
            operations()          
        elif level=="h":
            print("\n"*50)
            print(hard_logo)
            print("You have 5 attempts")
            operations()

game()  # To run function
















