
from random import randint
EASY_LEVEL_TURN= 10
HARD_LEVEL_TURN=5
#a function to check user's guess against actual answer
def check_answer(guess , answer):
    if guess>answer:
        print("Too high")
    elif guess<answer:
        print("Too low")
    else:
        print(f"you got it. your answer was {answer}")

# make function to choose difficulty easy or hard
def set_difficulty():
    level=input("Choose a difficulty . Type 'Easy' or 'Hard' ")
    if level=='Easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN
    
 #reapeating the guessing functionality if theey get wrong

def game():
    print("Welcome to the Number Guessing Game! ")
    print("I m thinking if a number between 1 and 100. ")
    answer=randint(1,100)

    turns=set_difficulty()
    print(f"you have {turns} attempts remaining to guess the number.")

    guess=0
    while guess!=answer:
        


    #let user gues a number
     guess=int(input("Make a guess: "))
     check_answer(guess,answer)

game()

#track the number of turns and reduce by 1 if they get wrong


