import random
import time

#initialise score
wins = 0
losses = 0

#initialise round
round = 0

#create dictionary for options
options_key = { 'r': 'rock' ,
                's': 'scissors',
                'p': 'paper' }

#invite player to game
print('Hello, welcome to rock paper scissors!')
time.sleep(1)

while True:
    start = input('Type START to continue or QUIT to exit: ').upper()

    # starting the game
    if start == 'START':
        options = ['r', 'p', 's']
        round += 1
        print(f'Round {round}!')

        # user choice
        user_choice = input('Enter your choice (rock [r], paper [p], or scissors [s]): ').lower()

        while user_choice not in options:
            user_choice = input('Invalid choice, please enter rock [r], paper [p], or scissors [s]: ').lower()

        user_choice_full = options_key[user_choice]

        # Computer’s choice
        computer_choice = random.choice(options)
        computer_choice_full = options_key[computer_choice]

        # Display choices
        print(f'You chose: {user_choice_full}')
        print(f'The computer chose: {computer_choice_full}')

        # Display outcome
        if user_choice == computer_choice:
            print("It's a tie!")

        elif (user_choice == 'r' and computer_choice == 's') or \
                (user_choice == 'p' and computer_choice == 'r') or \
                (user_choice == 's' and computer_choice == 'p'):
            print('You win!')
            wins += 1

        else:
            print('You lose!')
            losses += 1

        # Display current score
        print(f'Current score: Wins= {wins} Losses= {losses}')
        time.sleep(1)

    #end game
    elif start == 'QUIT': #ends the game
        print('Goodbye!')
        break
    else:
        continue