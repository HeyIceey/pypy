import sys, os, random, time, pygame, string # Importing Libraries (Some of them are no longer needed with the current version)
print("\033c")

# Hangman Game 
# 28 March 2023 | 8:42 AM

# Any comment with nothing under it has been moved, pls ignore it :)
# ------------------------------------------------------------------------------------------------------------------------------------------ #

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
t = 1.1 # Increased Speed So It loads faster
st = 0.02
def sp(str):
        DeprecationWarning
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(st)
        time.sleep(t)
while True: # Word List
    words = ["april", "banana", "cherry", "date", "berry", "fan", "grape", "honey", "kiwi", "lemon", "mango", "flower", "orange", "peach", "queen", "king", "mouse", "star", "water", "Kwantlen", "Rai", "Zimmerman"]

    # Messages for correct and incorrect guesses
    correct_msgs = ["Well done!", "Excellent!", "Good job!", "YESSS! LET'S GO!", "Nice one!", "Keep it up!", "You're Legendary!", "AYYYY!", "You Got It!", "Damn you're good!", "LET'S DO IT!"]
    incorrect_msgs = ["Oops! Try again!", "Skill Issue? Try again!", "Naa! Try again!", "You're running out of lives my friend!", "LOL You suck, try again!"]
                
    # Defining The Game Function

    def hangman():
                guessed_letters = []
                incorrect_guesses = 0
                word = random.choice(words)

                # Remove "Rai" and "Zimmerman" from the word list
                while word == "Rai" or word == "Zimmerman":
                    word = random.choice(words)
                

                correct_letters = []
                

                
                for i in word:
                    if i not in correct_letters:
                        correct_letters.append(i)
                        
                    elif i in correct_letters:
                        continue

    
    # Create a string to represent the hidden word
                hidden_word = "_" * len(word)
                sp("Let's start!\n")
                print("The word has", len(word), "letters.\n")

                # Game loop
                while True:
                    if "_" not in hidden_word and incorrect_guesses < 6:
                            print("               ") # Spacing
                            sp("Congratulations, you actually won!!!!!\n")
                            print("               ")

                            time.sleep(1)
                            # Winning Condition (Play Again?)
                            play_again = input("Do you want to play again? (y/n)   ").lower() 
                            if play_again == "y":
                                # Reset the game
                                print("\033c")
                                hangman()  
                            elif play_again == "n":
                                sp("Goodbye then!\n")
                                quit()
                            else:
                                sp("I'll take that as a no! Bye Bye!\n")
                                quit()
                    
                    # Ask the user to guess a letter
                    sp("            \n") # Spaces For Clean Appearance
                    guess = input("Guess a Letter: ").lower()
                    sp("            \n")

                    if guess in alpha:
                        
                    
                        # Text set for Already Guessed Letter 
                        already_guessed = ["You've already guessed it Lmao, Do it again!", "You Guessed it already bro, Try again!", "Buddy don't you know any other letters? Type again!"]
                        if guess in guessed_letters:
                            sp(random.choice(already_guessed))
                            continue
                        

                        # Add the letter to the guessed letters list
                        guessed_letters.append(guess)
                         

                        # Check if the letter is in the word
                        if guess in word:
                            print(random.choice(correct_msgs))
                            # Update the hidden word
                            for i in range(len(word)):
                                if word[i] == guess:
                                    hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]                                                                                                                                                                                
                        else:
                            print(random.choice(incorrect_msgs))
                            # Display the current state of the hidden word
                            print(hidden_word)
                           
        
                            # Hangman Drawings :)
                            incorrect_guesses += 1
                            if incorrect_guesses == 1:
                                
                                print("   ___ ")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("__|__  ")
                                time.sleep(1.5)
                            elif incorrect_guesses == 2:
                                print("   ___ ")
                                print("  |   |")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("__|__  ")
                                time.sleep(1.5)
                            elif incorrect_guesses == 3:
                                print("   ___ ")
                                print("  |   |")
                                print("  |   O")
                                print("  |    ")
                                print("  |    ")
                                print("  |    ")
                                print("__|__  ")
                                time.sleep(1.5)
                            elif incorrect_guesses == 4:
                                print("   ___  ")
                                print("  |   | ")
                                print("  |   O ")
                                print("  |   | ")
                                print("  |   | ")
                                print("  |     ")
                                print("__|__   ")
                                time.sleep(1.5)
                            elif incorrect_guesses == 5:
                                print("   ___  ")
                                print("  |   | ")
                                print("  |   O ")
                                print("  |  /|\ ")
                                print("  |   | ")
                                print("  |     ")
                                print("__|__   ")
                                sp("This is your Last Life!\n")
                                time.sleep(1.5)
                            elif incorrect_guesses == 6:
                                print("   ___  ")
                                print("  |   | ")
                                print("  |   O ")
                                print("  |  /|\\ ")
                                print("  |   | ")
                                print("  |  / \\ ")
                                print("__|__   ")
                                time.sleep(1.5)
                                sp("The man... was Hanged :(\n")
                                print("LOL YOU LOST :( | THE WORD WAS:", word) # SP wont work here as it only takes 1 sentence :(
                                
                                time.sleep(1)  
                                # Losing Condtion (Play Again?)
                                play_again = input("Do you want to play again? (y/n) ").lower() 
                                if play_again == "y":
                                    # Reset the game
                                    hangman()  
                                elif play_again == "n":
                                    quit()                
                                
                                else:
                                    sp("I'll take that as a no then!\n")
                                    quit()
                                                                                                        
                        # Display the current state of the hidden word and the guessed letters
                        print("Guessed letters:", ", ".join(guessed_letters))
                        sp(hidden_word)

                        # Add a delay before the next guess
                        time.sleep(1.1)
                        
                    else:
                        sp("That's not a valid Response man!\n")
                        sp("Try Again!\n")
                        continue
                                

    # Just a random intro warning :)
    sp("Loading Intro...\n")
    sp(".....\n")
    sp(".....\n")
    sp("Loaded...\n")
    sp("Launching!\n")
    time.sleep(1)
    print("\033c")

    # Intro
    sp("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n")
    sp("\033[36m" + "Starfall Studios Presents.." + "\033[0m \n")
    sp("An Articforce Production..\n") 
    sp("\033[36m" + "Also commonly known as Hangman" + "\033[0m \n")
    sp("Version 1.30.3\n")
    sp("\033[36m" + "BLAST OFF!" + "\033[0m \n")
    sp("★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★\n")


    time.sleep(2.5) # Wait 2.5 Seconds Before Clearing Terminal
    print("\033c") # Clear Termimal Again

    # Redifining Time Delay (Faster) For The Game:
    t = 0.5
    st = 0.01
    def sp(str):
        for letter in str:
            DeprecationWarning
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(st)
        time.sleep(t)


    while True: # While Loop For The Game

        while True:  # Starting Prompt
            sp("Press 'x' Begin the Game\n")
            sp("Press 'q' to Quit the Game\n")
            sp("Press 'i' for More Information\n")
            sp("Enter Your Choice Below:\n")
            choice = input("").lower() # So Both Upper/Lowecase Responses Work :)
            
            if choice == "i": # Game Rules
                sp("This is BLAST OFF By Starfall Studios \n")
                sp("Running On Version 1.3.30 \n")
                sp("Would you like to know about the game rules? \n")
                sp("y/n?\n") # Optional Choice
                choice = input("").lower()
                if choice == "y": # Game Rules
                    sp("Now Printing...\n")
                    sp("Game Rules:\n")
                    print("Hangman Rules:\n\n"
                    "- The computer will select a word.\n"
                    "- The user will guess one letter at a time.\n"
                    "- If the letter is in the word, the computer will display all instances of the letter in the word.\n"
                    "- If the letter is not in the word, the computer will draw one part of the hangman.\n"
                    "- The game ends when the user has correctly guessed all the letters in the word, or when the hangman is complete.\n"
                    "- The user is allowed a maximum of 6 incorrect guesses before the game is over.")
                    sp("Waiting 5 seconds before proceeding...\n")
                    time.sleep(5)
                    sp("Let's Choose Again!\n")
                    time.sleep(1)
                    sp("If you'd like to Clear the terminal, press C\n")
                    sp("If nothing is entered, Terminal will proceed within 6 seconds...\n")
                    player = input("").lower()
                    if player == "c":
                        print("\033c")
                    else:
                        time.sleep(6)
                    continue
                
            # If N is Pressed, User will be prompted to choose, again :)            
                if choice == "n": # Quit This Loop and Run Back 
                    print("\033c")
                    sp("Alright then, Let's Choose Again!\n")
                    break
            
            elif choice == "q": # Quit The Entire Thing :(
                sp("Quitting Now...\n")
                sp("Run Code Again To Start :)\n")
                sp("Goodbye...\n")
                quit()
                
            elif choice == "x": # Playing The Game (Previously had another q to quit and p to play option after pressing X, but that caused issues :(
                print("\033c") # Clear It Again :)           
                sp("Alright then! Let's get started :D \n")
                time.sleep(1.5) # Sorry, I just really wanted to do this :D
                print("\033c") # Loading The Thing (Idk it just seemed cool)
                time.sleep(1.2) # :D
                # Cleared The Terminal, once again
                print ("\033c")
                
                # Seperate Time Delay For Hangman Pictures and Stuff :)
                t = 0.05
                st = 0.001
                                        
                # Start the game
                
                sp("Welcome to Hangman!\n")
                sp("We'll start by guessing a random letter\n" )
                sp("We'll continue to guess a random letter \n")
                sp("You have exactly 6 Lives, if you guess wrong 6 times, you'll lose :)\n")
                sp("A Hangman picture will be drawn with your first incorrect guess.\n" )
                sp("A Picture will not be drawn if you guess correct.\n" )
                time.sleep(2)
                print("\033c")
                
                time.sleep(4)
            
                hangman()
                                
            else:
                        # If an Invalid Response is received
                        sp("Invalid Response Bro, Choose Again! :) \n")
                        continue # Start the loop again 

# The End