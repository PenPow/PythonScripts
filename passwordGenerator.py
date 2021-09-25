from random import randrange
from sys import exit
from utils import colors, console

characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM?:;#!£$%^&*()_-+='

def main():
  length = console.input(f'{colors.HEADER}How long do you want the generated password to be?{colors.RESET} ')
  i = 1

  str = ''

  try:
      length = int(length)
  except:
      console.log(f'{colors.FAIL}Error! Please restart')
      exit(1)

  while i < (int(length) + 1):
      str = str + characters[randrange(0, len(characters))]
      i+=1

  console.log(f'{colors.OKGREEN}Your password is{colors.RESET} {str}')

  if console.input(f'{colors.HEADER}Do you want to save this to a file (y/n){colors.RESET} ').lower() == 'y':
      with open('output/password.env', 'w') as file:
          fileContents = f'# Don\'t Share this File, as it contains the latest generated password\npassword = {str}'
          file.write('')
          file.write(fileContents)
          file.close()

          console.log(f'{colors.HEADER}Saved to \'./output/password.env\'')

  exit(0)

def start():
  with open("assets/passwordGeneratorWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
  start()