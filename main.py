import letterGame, passwordGenerator, stringManipulation, conditionalStatements, creditCardValidator, reverseIt, celciusToFahrenheit, fahrenheitToCelcius, snakeEyes
from utils import colors, console, strToInt, clear, clearDatabase

def main():
  inputGame = strToInt(input(f'{colors.HEADER}Please Select a Module to Load:{colors.RESET}\n{colors.OKBLUE}1){colors.RESET} Letter Game\n{colors.OKBLUE}2){colors.RESET} Password Generator\n{colors.OKBLUE}3){colors.RESET} String Manipulation\n{colors.OKBLUE}4){colors.RESET} Conditional Statements\n{colors.OKBLUE}5){colors.RESET} Credit Card Validator\n{colors.OKBLUE}6){colors.RESET} Reverse It!\n{colors.OKBLUE}7){colors.RESET} Celcius to Fahrenheit\n{colors.OKBLUE}8){colors.RESET} Fahrenheit to Celcius\n{colors.OKBLUE}9){colors.RESET} Snake Eyes\n{colors.OKBLUE}10){colors.RESET} Reset Database\n\n{colors.HEADER}Input:{colors.RESET} '))

  clear()

  if inputGame == 1:
    console.log('Loading Letter Game!\n')
    letterGame.start()
  elif inputGame == 2:
    console.log('Loading Password Generator!\n')
    passwordGenerator.start()
  elif inputGame == 3:
    console.log('Loading String Manipulation!\n')
    stringManipulation.start()
  elif inputGame == 4:
    console.log('Loading Conditional Statements!\n')
    conditionalStatements.start()
  elif inputGame == 5:
    console.log('Loading Credit Card Validator!\n')
    creditCardValidator.start()
  elif inputGame == 6:
    console.log('Loading Reverse It!\n')
    reverseIt.start()
  elif inputGame == 7:
    console.log('Loading Celcius to Fahrenheit!\n')
    celciusToFahrenheit.start()
  elif inputGame == 8:
    console.log('Loading Fahrenheit to Celcius!\n')
    fahrenheitToCelcius.start()
  elif inputGame == 9:
    console.log('Loading Snake Eyes!\n')
    snakeEyes.start()
  elif inputGame == 10:
    clearDatabase()
    clear()
    console.log(f'{colors.FAIL}Cleared{colors.RESET} Database!\n')
    main()
  else:
    console.log('Invalid Option!\n')
    main()

if __name__ == '__main__':
  main()