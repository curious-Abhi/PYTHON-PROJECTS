
from art import logo,vs
from game_data import data
import random
from clrscreen import clear_screen


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

print(logo)
score=0
game_should_continue=True
account_b=random.choice(data)

while game_should_continue:
    account_a=account_b
    account_b=random.choice(data)
    
    while account_a==account_b:
       account_b=random.choice(data)  #genrate again new account b

    print(f"Compare A:{format_data(account_a)}")  
    print(vs)
    print(f"Against B:{format_data(account_b)}")  


    
    guess=input("Who has more followers ?Type 'A' or 'B' :").lower()


    a_follower_count=account_a['follower_count']
    b_follower_count=account_b['follower_count']
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
   
    clear_screen()
    print(logo)


    if is_correct:
        score +=1
        print(f"you are right! Current Score: {score}")

    else:
        game_should_continue=False
        print(f"sorry , that's wrong. Final score:{score}")

