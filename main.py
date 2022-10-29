# Display welcome message and instructions
print("======= TO BE HANGED OR NOT BE HANGED =======")
print()
print("Welcome to hangman! Today you will attempt to guess the secret word")
print("by entering a letter down below which will give you a hint to what the")
print("word is.  You have 5 attempts to guess the correct word.  Have fun!")
print()

# Create a define function that prompts the user to enter a letter
def getLetter():
  
  # Create a variable that holds a default value for the user's letter guess
  userLetter = ""
  
  # Create a while loop to get a single letter from the user
  while(len(userLetter) != 1):
    
    # Prompt the user to enter a letter
    userLetter = input("Enter a letter: ")
    
  # Return the user's letter
  return userLetter.upper()


# Create a function that displays the secret word
def getSecretWord(word, guesses):
 
  # Go through each letter in the secret word, and determine HOW we display it
  for letter in word:
 
    # If this letter (from the secret word) has been guessed, display the letter
    if(letter in guesses):
    
      print(letter, end=" ")
    # Otherwise, display an underscore ( _ )
    else:
      print("_", end=" ")


# Create a function that determines if the user has won the game
def hasUserWon(word, guesses):
 
  # Let's use an "Innocent Until Proven Guilty" Algorithm...
  # ...and create a variable that is set to "True"
  won = True
 
  # Go through each letter in the secret word
  for letter in word:
 
    # Check if the letter has been guessed
    if(letter not in guesses):
 
      # If it has NOT been guessed, set the variable we created to False, and stop the loop
      won = False
      break
 
  return won


# Create a secret word
correctWord = "philadelphia"

# Make sure the secret word is all upper case
correctWord = correctWord.upper()

# Create collection to store user guesses
guessList = []

# Create a variable to store the number of strikes
userStrikes = 0


# If the user has NOT won OR lost, take a turn
while(userStrikes < 5 and not hasUserWon(correctWord, guessList)):
  guesses = getLetter()
  # Store the guess
  guessList.append(guesses)
  print()
  # Determine if this letter is in the secret word
  if(guesses in correctWord):
    print("Good Guess!")
    print()
    getSecretWord(correctWord, guessList)
    print()
  else:
    userStrikes += 1
    print(f"Sorry you guessed wrong, you have {userStrikes} out of 5 strikes")

if(userStrikes > 4):
  print(f"The secret word was {correctWord}")
  
else:
  print(f"Congratulations! You have guessed the correct word which is: {correctWord}")
