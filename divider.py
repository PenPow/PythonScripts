from utils import strToInt, console, colors

def main():
    numberToDivide = strToInt(console.input(f'{colors.RESET}Which Number Should I {colors.FAIL}Divide{colors.RESET}?{colors.OKBLUE} '), True)

    numberDivider = strToInt(console.input(f'{colors.RESET}Which Number Should I {colors.FAIL}Divide By{colors.RESET}?{colors.OKBLUE} '), True)

    if numberToDivide == None or numberDivider == None or numberDivider == 0:
      console.log(f'{colors.FAIL}Invalid{colors.RESET} Number - Please only Input Numbers')
      main()
    else:
      if numberToDivide % numberDivider == 0:
        console.log(f'\n{colors.RESET}{numberToDivide} is {colors.OKGREEN}exactly divisible{colors.RESET} by {numberDivider}!')
        main()
      else:
        console.log(f'\n{colors.RESET}{numberToDivide} is {colors.FAIL}not divisible{colors.RESET} by {numberDivider} - Remainder of {round(numberToDivide % numberDivider)}!')
      
      main()

def start():
  with open("assets/dividerWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    main()