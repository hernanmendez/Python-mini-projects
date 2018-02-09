from random import randint
from functions import yes_no
from re import match

print('Welcome to the guess the number game')

def difference(num, guessedNum):
  isLower = False
  difference = num - guessedNum
  if difference < 0:
    difference *= -1
    isLower = True

  percentage = (difference / num) * 100
  
  msg = 'lower' if isLower else 'higher'
  if percentage >= 50:
    print(f'The number is way {msg}')
  elif percentage >= 10:
    print(f'The number is {msg} than that')
  else:
    print(f'The number is a little bit {msg}')

def isInt(string):
  return True if match('^\d+$', string) else False

def choosing(inputStr):
  while True:
    string = input(inputStr)
    if isInt(string):
      return int(string)
    else:
      print('Sorry I think what you typed wasn\'t a number')

if yes_no('Would you like to play?', [ 'Ok let\'s begin', 'Please come back and play!' ]):
  playing = True
  while playing:
    choosingNum = True
    while choosingNum:
      lowNum = choosing('Enter the lowest number you want to appear: ')
      highNum = choosing('Enter the highest number you want to apper: ')
      if lowNum > highNum:
        print('The lowest number cannot be higher than the highest number')
      else:
        choosingNum = False
    
    notChanged = True
    while notChanged:
      genNum = randint(lowNum, highNum)
      print('Random number generated')
      guessing = True
      while guessing:
        guessedNum = choosing('What do you think the number is?: ')
        if guessedNum == genNum:
          print('HOORAY you guessed correctly')
          guessing = False
        else:
          difference(genNum, guessedNum)
          guessing = not yes_no('Do you wanna give up?')
          if not guessing:
            print(f'The number was {genNum}')
      notChanged = yes_no('Play again?', 'See ya')
      playing = notChanged
      if playing:
        notChanged = yes_no('Do you want to keep the number range as it\'s?')