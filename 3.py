from functions import yes_no
from random import randint

print('Welcome to the madlibs generator')

# 0 = exclamation
# 1 = adverb
# 2 = noun
# 3 = adjective

templates = [
  '{0}! he said {1} as he jumped into his convertible {2} and drove off with his {3} wife.',
]

if yes_no('Would you like to play?', [ 'Ok let\'s begin', 'Please come back and play!' ]):
  playing = True
  while playing:
    string = templates[randint(0, len(templates) - 1)]
    exclamation = input('Enter an exclamation: ')
    adverb = input('Enter an adverb: ')
    noun = input('Enter a noun: ')
    adjective = input('Enter an adjective: ')
    print(string.format(exclamation, adverb, noun, adjective))
    playing = yes_no('Would you like to play again?', 'See ya')