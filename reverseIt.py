from utils import colors, console

vowels = ['a', 'e', 'i', 'o', 'u']

def main():
  message = console.input(f'{colors.HEADER}Please enter some text to reverse:{colors.RESET} ').lower()

  count = {
    'vowels': 0,
    'consonants': 0
  }

  palindrone = False

  if message == message[::-1]:
    palindrone = True

  for char in message:
    if char in vowels:
      count['vowels'] = count['vowels'] + 1
    else:
      count['consonants'] = count['consonants'] + 1

  console.log(f'{colors.HEADER}\nReversed String:{colors.RESET} {message[::-1]}\n{colors.HEADER}Vowel Count:{colors.RESET} {count["vowels"]}\n{colors.HEADER}Consonant Count:{colors.RESET} {count["consonants"]}\n{colors.HEADER}Palindrome Status:{colors.RESET} {palindrone}')

  main()

def start():
  with open("assets/reverseItWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

  main()

if __name__ == '__main__':
  start()