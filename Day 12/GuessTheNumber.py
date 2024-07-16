import random
logo = """
  /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                                                                                                           
"""                                                                                                                                                        
#The hidden number
HiddenNumber = random.randint(1,100)


#Program Start
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
#print(f"Pssst, the correct answer is {HiddenNumber}")
Difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#Game Settings
if Difficulty == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
elif Difficulty == "hard":
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
else:
    print("error")

#Determining User Guess
def Guessing(Guess):
    if Guess > HiddenNumber:
        print("Too high.")
        print("Guess again.")
    elif Guess < HiddenNumber:
        print("Too low.")
        print("Guess again.")
    elif Guess == HiddenNumber:
        print(f"You got it! the answer was {HiddenNumber}")
        quit()


#User Guesses
GameEnd = False
while GameEnd == False:
    UserGuess = int(input("Make a guess: "))
    attempts -= 1
    Guessing(UserGuess)
    print(f"You have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print(f"You've run out of guesses, you lose. The correct answer was {HiddenNumber}.")
        quit()
