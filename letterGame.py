from nltk.corpus import words
import nltk
import sys

from replit import db

class console:
    def log(message):
        print(message)
    def input(message):
        return input(message)

def getDatabase(key):
    try:
        return db[key]
    except KeyError:
        return False

def setDatabase(key, value):
    db[key] = value
    return True

def parseCommand(command):
    command = command.lower().replace('.', '')
    if command == 'help':
        console.log(
            f'{colors.RESET}Current {colors.WARNING}Commands{colors.RESET}: {colors.OKCYAN}.top{colors.RESET} | {colors.OKCYAN}.help{colors.RESET} | {colors.OKCYAN}.exit{colors.RESET} | {colors.OKCYAN}.reset{colors.RESET}'
        )
    elif command == 'top':
        highScore = getDatabase('highScore')
        word = getDatabase('highScoreWord')
        if word:
            console.log(
                f'Your Highest Score is {colors.OKCYAN}{highScore}{colors.RESET} with word \'{colors.OKGREEN}{word}{colors.RESET}\''
            )
        else:
            console.log(
                f'{colors.RESET}You {colors.FAIL}don\'t{colors.RESET} have a high score!'
            )
    elif command == 'exit':
        console.log(f'{colors.OKGREEN}Exiting! Have a Nice Day')
        sys.exit(0)
    elif command == 'reset':
        setDatabase('highScoreWord', '')
        setDatabase('highScore', 0)
        console.log(f'{colors.FAIL}Resetting{colors.RESET} high score')
    else:
        console.log(f'{colors.FAIL}Invalid{colors.RESET} Command')

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

letterDict = {
    "A": 2,
    "B": 17,
    "C": 10,
    "D": 12,
    "E": 1,
    "F": 18,
    "G": 16,
    "H": 15,
    "I": 4,
    "J": 25,
    "K": 21,
    "L": 9,
    "M": 14,
    "N": 7,
    "O": 5,
    "P": 13,
    "Q": 26,
    "R": 3,
    "S": 8,
    "T": 6,
    "U": 11,
    "V": 22,
    "W": 20,
    "X": 23,
    "Y": 19,
    "Z": 24,
}

def main():
    word = (
        console.input(f'\n{colors.RESET}Please Provide A Word/Command: {colors.OKCYAN}'
              )).replace(' ', '')

    if word.startswith('.'):
        parseCommand(word)
        main()

    if not word.lower() in words.words():
        console.log(
            f'{colors.RESET}That is an {colors.FAIL}Invalid{colors.RESET} Word'
        )
        main()

    total = 0
    for char in word:
        try:
            total = total + letterDict[char.upper()]
        except:
            pass

    highScore = getDatabase('highScore')

    if not highScore:
        highScore = 0

    if total > highScore:
        console.log(
            f'{colors.RESET}{colors.OKGREEN}Congratulations{colors.RESET}! Your word is your {colors.OKCYAN}highest{colors.RESET} yet, at {colors.OKCYAN}{total}{colors.RESET} points!'
        )

        setDatabase('highScore', total)
        setDatabase('highScoreWord', word)
    else:
        console.log(
            f'{colors.RESET}Your word is worth {colors.OKCYAN}{total}{colors.RESET} points!'
        )
    main()

def start():
  nltk.download('words')
  with open("assets/letterGameWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  console.log(f'To see all {colors.WARNING}commands{colors.RESET}, type \'.help\'')
  highScore = getDatabase('highScore')
  word = getDatabase('highScoreWord')

  if word:
    console.log(
      f'Your Highest Score is {colors.OKCYAN}{highScore}{colors.RESET} with word \'{colors.OKGREEN}{word}{colors.RESET}\''
    )

  main()

if __name__ == '__main__':
    start()