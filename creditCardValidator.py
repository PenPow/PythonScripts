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

def main():
    card = list(console.input(f'{colors.HEADER}Please Enter a Credit Card Number:{colors.RESET} ').strip())

    lastDigit = card.pop()

    card.reverse()

    i = 0

    finalDigits = []

    for digit in card:
        if i % 2 == 0:
            digit = int(digit) * 2

            if digit > 9:
                digit = digit - 9
            
            finalDigits.append(digit)
        else:
            finalDigits.append(int(digit))

        i = i + 1

    total = int(lastDigit) + sum(finalDigits)
    
    if total % 10 == 0:
        console.log(f'{colors.OKGREEN}Valid Card!{colors.RESET}')
    else:
        console.log(f'{colors.FAIL}Invalid Card!{colors.RESET}')
    
    main()

def start():
  with open("assets/creditCardValidatorWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    start