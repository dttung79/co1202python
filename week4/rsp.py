# Rock Scissors Paper Game

import random as rd

playing = True
win_count = 0
balance = 100

while playing:
    user_choice = input("Enter your choice (rock, scissors, paper): ")
    bet_amount = int(input("Enter your bet amount: "))
    if user_choice not in ('rock', 'scissors', 'paper'):
        print("Invalid choice")
    elif bet_amount > balance or bet_amount < 0:
        print("Invalid bet amount")
    else:
        n = rd.randint(1, 3)
        comp_choice = 'rock' if n == 1 else 'scissors' if n == 2 else 'paper'
        print(f'Computer choice: {comp_choice}')
        if user_choice == comp_choice:
            print('Draw game')
        elif (user_choice == 'rock'     and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper')    or \
             (user_choice == 'paper'    and comp_choice == 'rock'):
            print('You win')
            win_count += 1
            balance += bet_amount
        else:
            print('You lose')
            balance -= bet_amount
        
        answer = input('Do you want to continue (y/n)? ')
        playing = balance > 0 and answer == 'y'

print(f'You won {win_count} times')
print(f'Your balance is {balance}')