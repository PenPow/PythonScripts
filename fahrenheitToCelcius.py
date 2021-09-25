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

def strToInt(inputMessage):
  try:
    return int(inputMessage)
  except:
    return None

def main():
  temperature = strToInt(console.input('Enter a Temperature in Fahrenheit: '))

  if temperature == None:
    console.log('Invalid Temperature - Please only Input Numbers')
  
  print((temperature - 32) * (5 / 9))

  main()

if __name__ == '__main__':
  main()