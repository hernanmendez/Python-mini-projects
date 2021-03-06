from re import match

def yes_no(question = 'Yes or no?', answers = []):
  processed = False
  yes = False
  isList = type(answers) is list
  while not processed:
    response = input(question + ' (y/n): ')
    if response == 'y':
      if isList and len(answers) == 2:
        print(answers[0])
      processed = True
      yes = True
    elif response == 'n':
      if isList and len(answers) == 2:
        print(answers[1])
      elif not isList:
        print(answers)
      processed = True
    else:
      print('sorry I didn\'t understand')
  return yes

def choosingInt(inputStr):
  while True:
    string = input(inputStr)
    if (True if match('^\d+$', string) else False):
      return int(string)
    else:
      print('Sorry I think what you typed wasn\'t a number')