from utils import console, colors

def main():
  console.log(f'\n{colors.HEADER}Running from 0-100 Inclusive')

  sumOfNumbers = {
    'total': 0,
    'odd': 0,
    'even': 0
  }
    
  for i in range(0, 101):
    sumOfNumbers['total'] += i

    if i % 2 == 0:
      sumOfNumbers['even'] += i
    else:
      sumOfNumbers['odd'] += i
    
  console.log(f'{colors.RESET}Sum (All Numbers) is {colors.OKBLUE}{sumOfNumbers["total"]}')
  console.log(f'{colors.RESET}Sum (Odd) is {colors.OKBLUE}{sumOfNumbers["odd"]}')
  console.log(f'{colors.RESET}Sum (Even) is {colors.OKBLUE}{sumOfNumbers["even"]}')

  name = console.input(f'\n{colors.HEADER}What Is Your Name?{colors.RESET} ')

  string = ''

  for char in name:
    string += f'{char} '
  
  console.log(f'{colors.RESET}Name (Split) is {colors.OKBLUE}{string}')

  console.log(f'\n{colors.HEADER}Squaring from 1 - 20?{colors.RESET} ')

  for i in range(1, 21):
    console.log(f'{colors.RESET}Square of {i} is {colors.OKBLUE}{i ** i}')

  console.log(f'\n{colors.HEADER}FizzBuzz{colors.RESET} ')
  for i in range(1, 101):
    string = ''
    if i % 3 == 0:
      string += 'Fizz'
    if i % 5 == 0:
      string += 'Buzz'
    
    console.log(f'{colors.RESET}Fizzbuzz of {i} is {colors.OKBLUE}{i if len(string) == 0 else string}')
  
  main()

def start():
  with open("assets/forLoopsWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
    main()