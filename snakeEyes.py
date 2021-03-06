from utils import colors, console, clear, setDatabase, getDatabase, databaseEnabled
from random import randrange

def turn(total, playerNo):
  playerDice = [randrange(1, 6), randrange(1, 6)]

  if playerNo == 1:
    color = colors.OKCYAN
  else:
    color = colors.OKBLUE

  for value in playerDice:
    if value == 1:
      console.log(f'\n{color}Player {playerNo}{colors.RESET} rolled a {colors.FAIL}1 {colors.RESET}({playerDice[0]}, {playerDice[1]})')
      return 0
    total = total + value

  console.log(f'\n{color}Player {playerNo}{colors.RESET} Rolls a {colors.OKGREEN}{playerDice[0]} {colors.RESET}and{colors.OKGREEN} {playerDice[1]}{colors.RESET}\nTheir {colors.OKCYAN}Total{colors.RESET} is {colors.OKGREEN}{total}\n')
  
  if promptAgain():
    return turn(total, playerNo)
  else:
    return total

def loop(playerOneBank, playerTwoBank, roundNo):
  playerOneBank = playerOneBank + turn(0, 1);

  console.log(f'{colors.OKCYAN}Player 1 Bank: {colors.RESET}{playerOneBank}')

  playerTwoBank = playerTwoBank + turn(0, 2);

  console.log(f'\n{colors.OKCYAN}Player 1 Bank: {colors.RESET}{playerOneBank}')
  console.log(f'{colors.OKBLUE}Player 2 Bank: {colors.RESET}{playerTwoBank}\n')

  console.input(f'Press {colors.OKGREEN}Enter{colors.RESET} to Move to the Next Round ')

  clear()
  showSplashScreen()

  if playerOneBank > 100 or playerTwoBank > 100:
    handleWinCondition(playerOneBank, playerTwoBank, roundNo)
  else:
    loop(playerOneBank, playerTwoBank, roundNo + 1)

def promptAgain():
  if console.input(f'{colors.RESET}Would you like to {colors.OKGREEN}continue?{colors.RESET} ({colors.OKGREEN}y{colors.RESET}/{colors.FAIL}n{colors.RESET}) ').lower() == 'y':
    return True;
  return False;

def handleWinCondition(playerOneBank, playerTwoBank, roundNo):
  highScore = 0
  lowestRound = 1000000
  if databaseEnabled():
    highScore = getDatabase('highScoreSnakeEyes')
    lowestRound = getDatabase('lowestRound') or 100

  if playerOneBank > highScore or playerTwoBank > highScore:
    console.log(f'{colors.OKGREEN}New High Score{colors.RESET} of {playerOneBank if playerOneBank > playerTwoBank else playerTwoBank}!')

    if databaseEnabled():
      setDatabase('highScoreSnakeEyes', playerOneBank if playerOneBank > playerTwoBank else playerTwoBank)
  
  if roundNo < lowestRound:
    console.log(f'{colors.OKGREEN}Shortest Game Yet!{colors.RESET} with {roundNo} rounds!')

    if databaseEnabled():
      setDatabase('lowestRound', roundNo)
  
  if playerOneBank > playerTwoBank:
    console.log(f'{colors.OKCYAN}Player One{colors.RESET} is the Winner: {playerOneBank} points')
  elif playerTwoBank > playerOneBank:
    console.log(f'{colors.OKBLUE}Player Two{colors.RESET} is the Winner: {playerTwoBank} points')
  else:
    console.log(f'{colors.FAIL}Its a Draw{colors.RESET} {playerOneBank} points')
  
  if console.input(f'{colors.RESET}Would you like to {colors.OKGREEN}play again?{colors.RESET} ({colors.OKGREEN}y{colors.RESET}/{colors.FAIL}n{colors.RESET}) ').lower() == 'y':
    clear()
    start()

def main():
  loop(0, 0, 1)

def start():
  showSplashScreen()
  
  highScore = None
  lowestRound = None

  if databaseEnabled():
    highScore = getDatabase('highScoreSnakeEyes')
    lowestRound = getDatabase('lowestRound')
  
  if highScore and lowestRound:
    console.log(
      f'Your Highest Score is {colors.OKCYAN}{highScore}{colors.RESET}\nThe shortest game lasted {colors.OKCYAN}{lowestRound}{colors.RESET} rounds!'
    )

  main()

def showSplashScreen():
  with open("assets/snakeEyesWelcome.txt", "r") as file:
    console.log(colors.HEADER + file.read() + f'\n{colors.RESET}')
    file.close()

if __name__ == '__main__':
    start()