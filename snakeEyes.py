from utils import colors, console

def main():
    pass

def start():
    with open("assets/creditCardValidatorWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    start()