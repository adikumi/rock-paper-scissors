# Rock, Paper, and Scissors Game in Python

# import necessary libraries

import random

# VARIABLES

options = ['ROCK', 'PAPER', 'SCISSORS'] # options
round = 0 # rounds counter

# 2 players - computer, human

computer = ''
human = ''

# points counter

computer_point = 0
human_point = 0

# GAME

print('ROCK - PAPER - SCISSORS THE GAME')
print('================================')
print('\n')
print('Hello, I am Aditya, enjoy playing the Game.')
print('\n')
input('PRESS any KEY to START.')
print('\n')

while (computer_point < 5 and human_point < 5) :

  print('===============================')
    
  round += 1
  print('Round ', round)
  
  computer = random.choice(options)
  human = input('Enter Your Choice : ').upper()

  if (human in options) :

    if (human == computer) :
      
      print('Draw.')
      print(f'Both choose {human}.')
    
    elif (human == 'ROCK' and computer == 'SCISSORS') or (human == 'PAPER' and computer == 'ROCK') or (human == 'SCISSORS' and computer == 'PAPER') :
      
      print('HUMAN Wins this Round.')
      print(f'You chose {human} and Computer chose {computer}.')
      human_point += 1
    
    elif (human == 'ROCK' and computer == 'PAPER') or (human == 'PAPER' and computer == 'SCISSORS') or (human == 'SCISSORS' and computer == 'ROCK') :
      
      print('COMPUTER Wins this Round.')
      print(f'Computer chose {computer} and You chose {human}.')
      computer_point += 1
    
    else :
      
      pass
    
    print('Score after Round ', round, ' :')
    print('Human = ', human_point)
    print('Computer = ', computer_point)
    
  else :
    
    print('Invalid Input. Try Again.')
    pass
    
  print('===============================')
  print('\n')

print('FINAL SCORE : ')
print('Human = ', human_point)
print('Computer = ', computer_point)
print('\n')

if (computer_point == 5) :
  print('COMUTER defeated YOU.')
  print('Better Luck Next Time.')
  print('\n')
else :
  print('YOU defeated COMPUTER.')
  print('CONGRATULATIONS.')
  print('\n')


# ROUGH SPACE

# else :
#     print('COMPUTER Wins this Round.')
#     print(f'Computer chose {computer} and You chose {human}.')
#     computer_point += 1

# ROUGH SPACE