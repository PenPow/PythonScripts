import letterGame, passwordGenerator, stringManipulation, conditionalStatements, creditCardValidator, reverseIt

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def strToInt(inputMessage):
  try:
    return int(inputMessage)
  except:
    return None

def main():
  inputGame = strToInt(input(f'{colors.HEADER}Please Select a Module to Load:{colors.RESET}\n{colors.OKBLUE}1){colors.RESET} Letter Game\n{colors.OKBLUE}2){colors.RESET} Password Generator\n{colors.OKBLUE}3){colors.RESET} String Manipulation\n{colors.OKBLUE}4){colors.RESET} Conditional Statements\n{colors.OKBLUE}5){colors.RESET} Credit Card Validator\n{colors.OKBLUE}6){colors.RESET} Reverse It!\n\n{colors.HEADER}Input:{colors.RESET} '))

  if inputGame == 1:
    print('Loading Letter Game!\n')
    letterGame.start()
  elif inputGame == 2:
    print('Loading Password Generator!\n')
    passwordGenerator.start()
  elif inputGame == 3:
    print('Loading String Manipulation!\n')
    stringManipulation.start()
  elif inputGame == 4:
    print('Loading Conditional Statements!\n')
    conditionalStatements.start()
  elif inputGame == 5:
    print('Loading Credit Card Validator!\n')
    creditCardValidator.start()
  elif inputGame == 6:
    print('Loading Reverse It!\n')
    reverseIt.start()
  else:
    print('Invalid Option!\n')
    main()

if __name__ == '__main__':
  main()