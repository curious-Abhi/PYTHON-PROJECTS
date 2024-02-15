
from random import randint
EASY_LEVEL_TURN= 10
HARD_LEVEL_TURN=5

#track the number of turns and reduce by 1 if they get wrong
turns=0
#a function to check user's guess against actual answer
def check_answer(guess , answer ,turns):
    if guess>answer:
        print("Too high")
        return turns -1
    elif guess<answer:
        print("Too low")
        return turns -1
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

    guess=0
    while guess!=answer:
     print(f"you have {turns} attempts remaining to guess the number.")
 #let user gues a number
     guess=int(input("Make a guess: "))
     turns=check_answer(guess,answer,turns)
     if turns==0:
         print("you have run out of guesses , you lose.")
         return
     elif guess!=answer:
         print("Guess Again")
        

game()




