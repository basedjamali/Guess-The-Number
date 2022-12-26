import random

print("=== This is a simple number guesser game === \n=== You have 3 chances to get the right number between 1 - 10 === \n\r")

def playAgain():
  play_again = input('\n\rDo you want to play again [y/n]: ')
  while True:
    if play_again == 'y':
      return guessTheNumber()
    else:
      print('See you next time :)')
      break

def guessTheNumber():
  userTries = 3
  computerChoice = random.randint(0, 10)

  while True:
    try:
      userChoice = int(input('Choose a number between 1-10: '))
    except ValueError:
        print('This is not a integer! Try again.')
        continue
    
    if userChoice != computerChoice:
      userTries -= 1
      print(f"Wrong! You have {userTries} tries remain.")
    if userTries == 0:
      print("You're out of chances! The right answer is: ", computerChoice)
      playAgain()
      break
    elif userChoice == computerChoice:
      print('You guessed the number right!')
      playAgain()
      break

guessTheNumber()


