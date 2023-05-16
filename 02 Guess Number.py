# Guessing Game | Two Variations, Computer Vs User - User vs Computer
# 4 PM | 28 February 2023
# 

import random  # Importing the random module
def guess(): # User Guesses The Number

    some_number = random.randint(1, 100)            
    guess = None
    while guess != some_number:
        guess = input("Guess a number between 1 and 100: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        if guess < some_number:
            print('Bad guess, guess again. It was too low')
        elif guess > some_number:
            print('Bad guess, guess again. It was too high')
    print("----------------------------------------------------------------")
    print(f"Congratulations! You guessed it. The number was {guess}.")
    print("----------------------------------------------------------------")


def cp_guess(x):  # Computer Guesses the Number

    low = 1
    high = 100
    feedback = ""
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high? or is it too low? or is it correct? (Type h/l/c): ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("----------------------------------------------------------------")
    print(f"Ayy I guessed your number, it was {guess}! Haha I'm so smart :)")
    print("----------------------------------------------------------------")
    

while True:  # Starting Prompt
    print("----------------------------------------------------------------------")
    print("I am Iceey, I'm a physic. I can guess what number you're thinking of.")
    print("If you're smart enough, try guessing a number I am thinking of.")
    print("Are you ready to see some magic?")
    print("Choose the game type, buddy :")
    print("1: User vs Computer")
    print("2: Computer vs User")
    print("Q: Quit (Please Don't, It took a long time to make.)")
    choice = input("Enter your choice (1/2/Q): ")
    print("----------------------------------------------------------------------")
    
    if choice == "1": # All Replies 
        print ("I have picked a Number between 1 and 100, You have to guess it. I will tell you if it's too high or low.")
        guess()
    elif choice == "2": 
        print ("Pick a number between 1 and 100, I will try to guess it. Let me know if it's too high, too low or Correct! Let's Go!")
        print ("Type h for high, l for low, or c for correct.")
        
        cp_guess(100)
    elif choice.lower() == "q":
        print ("Come on bro, it took me a long time to make this game. Goodbye!")
        break
    else:
        print("Invalid Choice, Try Again!")
print("-----------------------------------------------------------------------")

# End