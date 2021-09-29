from utils import colors, console, strToInt
from random import randrange

def main():
  diceSides = strToInt(console.input('What Sided Dice Should I Roll? '))
  diceRoll = strToInt(console.input(f'How Many Times Should I Roll This Dice? '))

  if diceSides != None and diceRoll != None:
    total = 0
    diceRolls = []
    for i in range(diceRoll):
      roll = randrange(1, diceSides)
      total = total + roll
      diceRolls.append(roll)
    
    diceRollString = ''

    for item in diceRolls:
      diceRollString = diceRollString + f'{item}, '
    
    console.log(f'You rolled {total} ({diceRollString[0:len(diceRollString) - 2]})')

def start():
  with open("assets/arithmeticOperatorsWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
  start()