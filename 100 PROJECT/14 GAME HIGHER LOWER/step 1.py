
from art import logo,vs
from game_data import data


def format_data(account):
    '''format player details in particular format'''
    account_name=account['name']
    account_desc=account['description']
    account_loc=account['country']
    return f'{account_name} , a {account_desc} , from {account_loc}'



#print the art
print(logo)


import random
#select player details randomly from game_data

account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)
print(f"Compare A:{format_data(account_a)}")  
print(vs)
print(f"Compare B:{format_data(account_b)}")  

#format player details in particular format
#account_name=account_a['name']
#account_desc=account_a['description']
#account_loc=account_a['country']
#print(f'{account_name} , a {account_desc} , from {account_loc}')

'''but similar things again have to do with account_b . so aviod repition , make function instead '''
#creation of function go up


#guess who has more follower


#if user guess is wrong first check 

#get follower of each player for comparing


#check if user is correct using if statement


#give user feedback on their guess


#track score 

#game repeat when user guess is correct

#making account at b position in next rounds

#clr screen


#