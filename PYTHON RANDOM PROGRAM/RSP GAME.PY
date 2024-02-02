import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      'Rock vs Paper -> Paper wins\n'
      'Rock vs Scissors -> Rock wins\n'
      'Paper vs Scissors -> Scissors wins\n')

while True:
    print("Enter your choice\n1 - Rock\n2 - Paper\n3 - Scissors\n")
    choice = int(input("Enter your choice: "))

    while choice not in [1, 2, 3]:
        choice = int(input('Enter a valid choice please: '))

    choices = ['Rock', 'Paper', 'Scissors']
    choice_name = choices[choice - 1]

    print('User choice is', choice_name)
    print('Now it\'s Computer\'s Turn....')

    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice - 1]

    print("Computer choice is", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('It\'s a Draw')
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print('Paper wins =>', end="")
        result = 'Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print('Rock wins =>', end="")
        result = 'Rock'
    else:
        print('Scissors wins =>', end="")
        result = 'Scissors'

    if result == 'DRAW':
        print("<== It's a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans != 'y':
        break

print("Thanks for playing")
