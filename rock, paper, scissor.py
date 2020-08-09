'''this code is about a game called rock, paper, scissor.
in this code the user is allowed to input their personal details
such as first name, last name, prefered user name, age, and sex.
the user can then pick a number from 1-3 while the computer gets to pick randomly'''
import random #import random
import time
def paper():
    print("hello sunshine! Welcome to the ROCK, PAPER, AND SCISSOR GAME!")
    first_name = str(input("enter first name: "))
    last_name = str(input("enter last name: "))
    username = (input("prefered username: "))
    age = int(input("your age: "))
    print("sex (male/female)")
    answer = input()

    if answer == 'male':
        print("male")
    else:
        print("female")

    print("winning rules of the ROCK, PAPER, SCISSOR game as follows: \n", "Rock vs paper -> paper wins\n",
          "Rock vs paper -> Rock wins\n"
          "paper vs scissor -> scissor wins\n")
    print("There are 3 choices to pick from")
def start():
    while True:
        print("Enter choice\n 1. Rock\n 2. paper\n 3. scissor\n")
        choice = int(input("your turn:"))
        whil e choice > 3 or choice < 1:
            choice = int(input("Enter your choice: "))
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'paper'
        else:
            choice_name = 'scissor'
        print("your choice is: ", choice_name)
        print("\n Now it's computer's turn....")
        computer_choice = random.randint(1, 3)
        while computer_choice == choice:
            computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice_name = 'Rock'
        elif computer_choice == 2:
            computer_choice_name = 'paper'
        else:
            computer_choice_name = 'scissor'
        print("computer's choice is: ", computer_choice_name)
        print(choice_name, "VS", computer_choice_name)

        if (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1):
            print("paper wins =>", end="")
            result = "paper"
        elif (choice == 1 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
            print("Rock wins =>", end="")
            result = "Rock"
        else:
            print("scissor wins =>", end="")
            result = "scissor"
        if result == choice_name:
            print(" Hurray! you are the winner  ")
        else:
            print(" oh oh computer wins ")
        print("Do you want to play again?")
        answer = input()
        if answer == "no" or "No" or "N" or "n":
            print("Thanks for playing! you can leave the game, hope to see you soon")
        else:

            print("you can continue the game")
            return




paper()











