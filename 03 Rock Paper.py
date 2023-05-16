import random, time, sys # Importing the Crucial Library
# RPSLS = Rock Paper Scissors Lizard Spock Game
# 11 AM | 8 March 2023

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- 

# Time Delay [Good For Text in Terminal]
t = 0.8 
st = 0.02 

def sp(str):
    for letter in str:
        DeprecationWarning
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)
    time.sleep(t)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
    
print("\033c") # Clears The Terminal 
print("\033[47m\033[31m Welcome! Let's Get Started! :)\033[0m")

print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
sp("\033[32m" + "Made By Himanish" + "\033[0m\n") # Testing Colors
sp("Hello there! My name is Iceey and I am a " + "\033[31m" + "RPSLS Champion." + "\033[0m\n")
sp("Welcome To  RPSLS!\n")               
sp("What is RPSLS? It is a Rock Paper Scissors Spock Lizard Game!\n")
print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
sp("\033[32m" + "Are you ready then? Lets play :)" + "\033[0m\n")
sp("\033[32m" + "Note: The computer will choose its move when you choose yours. The results will be printed afterwards." + "\033[0m\n")

def is_win(user, opponent):  # Defining Conditions For What Defeats What 
        if (user == "r" and opponent == "s") or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'l') or (user == 'l' and opponent == 'sp') or (user == 'sp' and opponent == 'r') or (user == 'r' and opponent == 'l') or (user == 'l' and opponent == 's') or (user == 's' and opponent == 'sp') or (user == 'sp' and opponent == 'p') or (user == 'p' and opponent == 'r'):
            return True
        return False

def s(): # So I dont need to change the s() command one by one after each print (or sp) statement
    time.sleep(0.8)
    
# Doing it again for the other section of code
t = 0.2
st = 0.01
def sp(str):
    for letter in str:
        DeprecationWarning
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)
    time.sleep(t)

wins = 0
while True:

    while True:  # Starting Prompt
        print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
        sp("\033[32m" + "Okay So," + "\033[0m\n")
        sp("If you want to know the game rules, press 'i'.\n")
        sp("If you want to play the game, press 'x'.\n")
        sp("If you want to quit, press 'q'.\n")
        sp("If you want to see a surpise, press 's'.\n")
        sp("Enter your choice:\n")
        choice = input("").lower()
        print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
        
        if choice == "i": # Game Rules
            print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
            sp("\033[31m" + "This will take while.., Enjoy!" + "\033[0m\n")
            sp("Okay, Here is what you need to know:\n")
            s()
            sp("Scissors cut Paper\n")
            s()
            sp("Paper covers Rock\n")
            s()
            sp("Rock crushes Lizard\n")
            s()
            sp("Lizard poisons Spock\n")
            s()
            sp("Spock smashes Scissors\n")
            s()
            sp("Scissors decapitates Lizard\n")
            s()
            sp("Lizard eats Paper\n")
            s()
            sp("Paper disproves Spock\n")
            s()
            sp("Spock vaporizes Rock\n")
            s()
            sp("Rock smashes Scissors\n")
            s()
            sp(" and let me ask you again then,\n")
            print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
        elif choice == "s": # Just me, testing background colors and text combos
            sp("\033[1;37;41m Why do programmers prefer dark mode? \033[m\n")
            sp("\033[1;37;41m Because light attracts bugs! \033[m\n")
            sp("\033[1;37;41m Okay okay sorry for the bad joke :( \033[m\n")
            sp("\033[1;37;41m Go ahead choose again! \033[m\n")

        
        elif choice == "x":  # If User Wants To Play 
            computer_choice = random.choice(['r', 'p', 's', 'l', 'sp']).lower()
            
            if computer_choice == 'r':
                computer = "Rock"
            elif computer_choice == 'p':
                computer = "Paper"
            elif computer_choice == 's':
                computer = "Scissors"
            elif computer_choice == 'l':
                computer = "Lizard"
            elif computer_choice == "sp":
                computer = "Spock" 
                
            sp("Choose your move " + "\033[31m" + "(r)ock | (p)aper | (s)cissors | (l)izard | (sp)ock" + "\033[0m\n")
            s()
            user = input()
            
            print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
        
            sp(f"The computer chose: {computer}\n")
        # Would normally put another seperator line here but The next one already does it :)
    
            if user == computer_choice:
                s()
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
                sp("THAT'S A TIE YOOOOOOO NOOO WAYYYY | RARE\n")   
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
            elif is_win(user, computer_choice) == True:
                s()
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
                sp("YOU JUST WON! YOOOO DAAAAAAAMNNNN | CLEAR W\n")
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
                wins += 1  # Wins
                sp(f"Total Wins: {wins}\n")
    
            elif is_win(user, computer_choice) == False:
                s()
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
                sp("YOU JUST LOST! HAHAHAHA TOO BADD | CLEAR L\n")
                print("♛┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅♛")
                
            sp("That was a great game!\n")
            sp("I will ask you if you want to play again, quit or would like to know the rules.\n")
            
        elif choice == "q":
            s()
            sp("\033[31m" + "It took quite a long to make this. You should really play this!" + "\033[0m\n")
            s()
            sp("\033[31m" + "Goodbye For Now, I'll see you later!" + "\033[0m\n")
            quit() # Code Stops Working, Re-Run to Continue
            
# End Of Code :)
# Bye Bye!
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------