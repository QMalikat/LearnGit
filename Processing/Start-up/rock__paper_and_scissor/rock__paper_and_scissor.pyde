import random
winner = ' '
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'Rock'
elif random_choice == 1:
    computer_choice = 'Paper'
else:
    computer_choice = 'Scissors'
    
#user choice
user_choice = input('Rock, paper or scissor? ')
if (user_choice != 'Rock' and
    user_choice != 'Paper' and
    user_choice != 'Scissors'):
    user_choice = imput('rock, Paper or Scissors? ')
print('User chose', user_choice)


#Computer finds the winner 
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'Paper' and user_choice == 'Rock':
    winner = 'Computer'
elif computer_choice == 'Rock' and user_choice == 'Scissors':
    winner = 'Computer'
elif computer_choice == 'Scissors' and user_choice == 'Paper':
    winner = 'Computer'
else:
    winner = 'User'

#Print command
    if winner == 'Tie':
        print('We both chose', computer_choice + ',play again.')
    else:
        print(winner, 'won. The computer chose', computer_choice + '.')
    
