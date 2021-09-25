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
    message = console.input(f'{colors.HEADER}What is your full name:{colors.RESET} ')

    try:
      message.split(' ')[1]
    except IndexError:
      console.log(f'{colors.FAIL}Invalid Name')
      main()

    string = f'''
    {colors.HEADER}Usage of .upper:{colors.RESET}
    {message.upper()}

    {colors.HEADER}Usage of .lower:{colors.RESET}
    {message.lower()}

    {colors.HEADER}Usage of len():{colors.RESET}
    {len(message)}

    {colors.HEADER}Concatenating Strings:{colors.RESET}
    {message + ' is your name'}
    {colors.HEADER}OR{colors.RESET}
    {f'{message} is your name'}

    {colors.HEADER}Converting a Number -> String:{colors.RESET}
    {str(100)} {colors.OKCYAN}(Using an f string interpolation automatically stringifies it){colors.RESET}

    {colors.HEADER}String Slicing:{colors.RESET}
    {f'The first character of your name is {message[0]}'} {colors.OKCYAN}(All strings are arrays in python, arrays start at 0 like in JavaScript){colors.RESET}
    {f'The first 5 letters of your name are {message[0:5]}'}

    {colors.HEADER}Using .find:{colors.RESET}
    {f'Your name contains the word "hello" at position {message.lower().find("hello")}'} {colors.OKCYAN}(-1 Indicates No Result Found){colors.RESET}
    '''

    console.log(string)

    console.log(f'''{colors.HEADER}Name Splitting:{colors.RESET}
        {colors.HEADER}Forename:{colors.RESET} {message.split(' ')[0]}{colors.RESET}
        {colors.HEADER}Surname:{colors.RESET} {message.split(' ')[1]}{colors.RESET}
    ''')

    tasks(message)

def tasks(message):
    firstCity = console.input(f'{colors.HEADER}Please enter a city name:{colors.RESET} ')
    secondCity = console.input(f'{colors.HEADER}Please input another city name:{colors.RESET} ')

    if firstCity.lower() == secondCity.lower():
        console.log(f'{colors.FAIL}Please choose 2 different cities\n{colors.RESET}')
        tasks();

    console.log(f'{colors.OKCYAN}{stringModifer(firstCity)}-{stringModifer(secondCity)}{colors.RESET}\n')

    tasks(message)

def stringModifer(string):
    return string[0:4].upper()

def start():
  with open("assets/stringManipulationWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    start()
