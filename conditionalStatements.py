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

class console:
    def log(message):
        print(message)

    def input(message):
        return input(message)

def strToInt(inputMessage):
  try:
    return int(inputMessage)
  except:
    return None

def main():
  message = strToInt(console.input(f'{colors.HEADER}What Temperature is it:{colors.RESET} '))

  if message == None:
    console.log(f'{colors.FAIL}Invalid Temperature')
  elif message >= 100:
    console.log(f'{colors.FAIL}Your water is boiling!')
  elif message <= 0:
    console.log(f'{colors.OKBLUE}Your water is freezing!')
  else:
    console.log(f'{colors.RESET}Your water is still a liquid!')
  
  message = strToInt(console.input(f'\n\n{colors.HEADER}Nitrate Level (0-50):{colors.RESET} '))

  if message == None or message > 50 or message < 1:
    console.log(f'{colors.FAIL}Invalid Level')
  elif message > 10:
    console.log(f'{colors.OKBLUE}Dose: 3ml')
  elif message > 2.5:
    console.log(f'{colors.OKBLUE}Dose: 2ml')
  elif message > 1:
    console.log(f'{colors.OKBLUE}Dose: 1ml')
  else:
    console.log(f'{colors.OKBLUE}Dose: 0.5ml')
  
  main()

def start():
  with open("assets/conditionalStatementsWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    start()
