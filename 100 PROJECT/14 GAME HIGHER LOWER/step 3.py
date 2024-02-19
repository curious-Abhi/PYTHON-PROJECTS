
from art import logo,vs
from game_data import data
import random


def format_data(account):
    '''format player details in particular format'''
    account_name=account['name']
    account_desc=account['description']
    account_loc=account['country']
    return f'{account_name} , a {account_desc} , from {account_loc}'

def  check_answer(guess,a_followers,b_followers):
    '''take user guess and followers of both account and return if right that situation only otheroise false'''
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"



#print the art
print(logo)
score=0
game_should_continue=True

#making game repeatable
while game_should_continue:

    #select player details randomly from game_data
    account_a=random.choice(data)
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A:{format_data(account_a)}")  
    print(vs)
    print(f"Against B:{format_data(account_b)}")  


    #guess who has more follower
    guess=input("Who has more followers ?Type 'A' or 'B' :").lower()

    #if user guess is wrong first check ,first know thw follower
    #get follower of each player for comparing
    #check if user is correct using if statement cretae function bove for this
    a_follower_count=account_a['follower_count']
    b_follower_count=account_b['follower_count']
    is_correct=check_answer(guess,a_follower_count,b_follower_count)


    #give user feedback on their guess
    #track score 
    if is_correct:
        score +=1
        print(f"you are right! Current Score: {score}")
    else:
        game_should_continue=False
        print(f"sorry , that's wrong. Final score:{score}")


#making account at b position in next rounds


#clr screen


#