try:
    from replit import db
except ModuleNotFoundError:
    pass

import os

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

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def getDatabase(key):
    try:
        return db[key]
    except KeyError:
        return False

def setDatabase(key, value):
    db[key] = value
    return True

def clearDatabase():
  for key in db.keys():
    del db[key]

def strToInt(inputMessage, convert = False):
  try:
    if convert:
      return float(inputMessage)
    else:
      return int(inputMessage)
  except:
    return None