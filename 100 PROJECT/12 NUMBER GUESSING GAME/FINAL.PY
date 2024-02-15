
from random import randint
from art import logo
EASY_LEVEL_TURN= 10
HARD_LEVEL_TURN=5

turns=0

def check_answer(guess , answer ,turns):
    if guess>answer:
        print("Too high")
        return turns -1
    elif guess<answer:
        print("Too low")
        return turns -1
    else:
        print(f"you got it. your answer was {answer}")

def set_difficulty():
    level=input("Choose a difficulty . Type 'Easy' or 'Hard' ")
    if level=='Easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN
    

def game():
    print(logo)
    print("Welcome to the Number Guessing Game! ")
    print("I m thinking if a number between 1 and 100. ")
    answer=randint(1,100)

    turns=set_difficulty()

    guess=0
    while guess!=answer:
     print(f"you have {turns} attempts remaining to guess the number.")
 
     guess=int(input("Make a guess: "))
     turns=check_answer(guess,answer,turns)
     if turns==0:
         print("you have run out of guesses , you lose.")
         return
     elif guess!=answer:
         print("Guess Again")
        

game()




