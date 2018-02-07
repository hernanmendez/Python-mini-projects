from random import randint
from functions import yes_no
print('Welcome to the dice rolling simulator')

if yes_no('Would you like to play?', [ 'Ok let\'s begin', 'Please come back and play!' ]):
  playing = True
  while playing:
    print('The dice says: ' + str(randint(1,6)))
    playing = yes_no('Would you like to play again?', 'See ya')