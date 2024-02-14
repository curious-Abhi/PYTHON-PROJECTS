import random
#from clrscreen import clear_screen
from art import logo
def deal_card():
    '''return a random card from a deck. '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    
    if sum(cards)==21  and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score , computer_score):
    if computer_score==user_score:
        return "Draw"
    elif computer_score==0:
        return "You lose! 😞 Computer has Blackjack."
    elif user_score==0:
        return "You win! 😃 You have Blackjack."
    elif user_score>21:
        return "You lose! 😞 You went over 21."
    elif computer_score>21:
        return "You win! 😃 Computer went over 21."
    elif computer_score>user_score:
        return "You lose! 😞 Your score is lower."
    else:
        return "You win! 😃 Your score is higher."


def play_game():

    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"     Your cards: {user_cards} , current score:{user_score}")
        print(f"     Computer's first cards: {computer_cards[0]} ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card , type 'n' to pass: ")
            if user_should_deal == 'n':
                is_game_over = True
            elif user_should_deal == 'y':
                user_cards.append(deal_card())

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your Final hand : {user_cards} ,final score: {user_score}")
    print(f" Computer 's Final hand : {computer_cards} ,final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do You want to play a game of Blackjack? Type 'y' or 'n':   ") == 'y':
    play_game()
