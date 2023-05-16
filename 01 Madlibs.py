# Madlibs Game Project
# 22 February 2023
# Madlibs Game [HT]

# ----------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Just Variables and Inputs, Pretty Basic :)

# Start
while True: 

    print("-----------------------------------------")
    print("Choose a madlib game, buddy :")               # Starting Prompt
    print("1: School Madlib")
    print("2: Confusing Madlib")
    print("3: Goofy Madlib")
    print("Q: Quit(You Can't, BTW)")
    choice = input("Enter your choice (1/2/3/Q): ")
    print("-----------------------------------------")
    
     # Madlib 1, The School Madlib
    if choice == "1":
        adj1 = input("Adjective: ")
        verb1 = input("A Verb(-ing): ")
        verb2 = input("A Verb: ")
        verb3 = input("A Verb(past): ")
        verb4 = input ("A Verb(past): ")
        verb5 = input("A Verb(past):")
        celebrity = input("Celebrity's Name: ")
        adj2 = input("Adjective: ")
        adj3 = input("Adjective: ")
        body1 = input ("A Body Part: ")
        place1 = input("A Place's Name: ")
        no1 = input("A Number: ")
        random1 = input("A Noun: ")          # "Random" = Used for Names/Specific Values Across All Madlibs | I added it afterwards :)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        madlib1 =  f"'School is really {adj1}! I love going there' said Husky. He really loved school and {verb1}. One day his {random1} showed him a goofy movie which said\
        'Did you know {verb2} water OR the school building or even eating entire {place1} does NOT makes you look like {celebrity}! Did you know school is full of {adj2} children,\
        who are also slightly {adj3}! After watching this {no1} hour long movie, Husky was very {verb3}! Husky used his {body1} and gave {random1} a\
        high-five. {random1} was {verb4} and they {verb5} Husky! It was a great experience!" 
      
        print(madlib1)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Madlib 2, The Confusing Madlib
    elif choice == "2":
        noun1 = input("Write A Noun: ")
        obj1 = input("An Object: ")
        noun2 = input ("A Noun: ")
        noun3 = input("A Noun: ")
        noun4 = input("A Noun: ")
        noun5 = input("A Noun: ")
        food1 = input("A Food Item: ")
        nn1 = input("A Small Number: ")
        vrb1 = input("A Verb: ")
        vrb2 = input("A Verb: ")
        vrb3 = input("A Verb: ")
        ad1 = ("An Adjective: ")
        ad2 = ("An Adjective: ")
       
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
        madlib2 = f"I asked my {noun1} why he was eating a {obj1}, it was {nn1} meters tall, and he said it was to keep his {noun2} warm. However, \
        he did not know the {noun3} was watching him. The {noun4} was drinking {food1} while the {noun5} was barking on {noun1}???\
         Suddenly, the {noun4} started to feel {ad1}, and he {vrb3} on the ground.\
         The {noun5} was still barking, but now he was also {vrb1}. My {noun1} looked at me and said, '{ad2}, isn't it?'"
        
        print(madlib2)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
 # Madlib 3, The Goofy Madlib
    elif choice == "3":
     aj1 =  input("Adjective: ")
     vr1 = input("Verb: ")
     vr2 = input("Verb: ")
     aj2 = input("Adjective: ")
     name = input("A Name: ")
     n1 = input ("A Name: ")
     vr3 = input ("Verb: ")
     objct1 = input("An Object: ")
     n2 = input("A Name: ")
     av1 = input("An Adverb: ")
     av2 = input("An Adverb: ")
     nn1 = input("A Number: ")
     
     print("------------------------------------------------------------------------------------------------------------------------------------------------------------")
     madlib3= f"It was a {aj1} day, everyone was {vr1} and {vr2}! The weather was surprisingly {aj2}! {name} was looking at the clouds, when they thought about {n1} \
     and {vr3} from the bed. They quickly grabbed the {objct1} and called the {n2}! They ran {av1} to the park and saw {nn1} {objct1}s {av2} flying in the sky.\
     They couldn't believe their eyes! They were confused and shocked!"
    
     print(madlib3)
     print("------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # Quit the game
    elif choice == "Q":
        print("------------------------------------")
        print("Thanks for playing!")
        print("------------------------------------")
        break

    # Invalid choice (Anything other than 1/2/3/Q)
    else:
     print("Invalid choice, choose again")

# End Of Code | Thanks 
# --------------------------------------------------------------------------------------------------------------------------------------------------------- #