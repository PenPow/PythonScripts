from utils import colors, console, strToInt

def main():
  temperature = strToInt(console.input(f'{colors.HEADER}Enter a Temperature in Fahrenheit:{colors.RESET} '))

  if temperature == None:
    console.log(f'{colors.FAIL}Invalid{colors.RESET} Temperature - Please only Input Numbers')
    main()
  
  console.log(f'Converted Temperature is {colors.OKGREEN}{(temperature - 32) * (5 / 9)}{colors.RESET}*C')

  main()

def start():
  with open("assets/fahrenheitToCelciusWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
  start()