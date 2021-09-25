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