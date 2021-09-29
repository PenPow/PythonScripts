from utils import colors, console, strToInt

def main():
  message = strToInt(console.input(f'\n{colors.HEADER}What Temperature is it:{colors.RESET} '))

  if message == None:
    console.log(f'{colors.FAIL}Invalid Temperature')
  elif message >= 100:
    console.log(f'{colors.FAIL}Your water is boiling!')
  elif message <= 0:
    console.log(f'{colors.OKBLUE}Your water is freezing!')
  else:
    console.log(f'{colors.RESET}Your water is still a liquid!')
  
  message = strToInt(console.input(f'\n\n{colors.HEADER}Nitrate Level (0-50):{colors.RESET} '), True)
  
  if message == None or message > 50 or message < 1:
    console.log(f'{colors.FAIL}Invalid Level')
  elif message >= 10:
    console.log(f'{colors.OKBLUE}Dose: 3ml')
  elif message >= 2.5:
    console.log(f'{colors.OKBLUE}Dose: 2ml')
  elif message >= 1:
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
