from utils import colors, console, strToInt

def main():
  temperature = strToInt(console.input(f'{colors.HEADER}Enter a Temperature in Celcius:{colors.RESET} '))

  if temperature == None:
    console.log(f'{colors.FAIL}Invalid{colors.RESET} Temperature - Please only Input Numbers')
    main()
  
  console.log(f'Converted Temperature is {colors.OKGREEN}{(temperature * (9 / 5)) + 32}{colors.RESET}*F')

  main()

def start():
  with open("assets/celciusToFahrenheitWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
  start()