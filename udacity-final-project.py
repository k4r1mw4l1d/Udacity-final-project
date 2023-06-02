# First import required libraries
import time
import random

# We create print_delay function to print text with delay
def print_delay(text):
    print(text)
    time.sleep(1)

# We create a function to start  
def game():
    while True:
        players_score = 0
        print_delay("Your car broke up and you have been looking for a mechanic")
        print_delay("You found a city serrounded with mist")
        print_delay("On your lift you found a sign with Silent hill written on it")
        print_delay("Do you want to go to city")
        print_delay("1 = Yes")
        print_delay("2 = No")
        option_1(players_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            print_delay("Thanks for playing and see you again")
            break


# We create a funtion for the player to choose his decision
def option_1(players_score):
    choice = input("Enter you choice (1/2): ")
    if choice == "1":
        city(players_score)
    elif choice == "2":
        keep_looking(players_score)
    else:
        print_delay("Please enter a valid option")
        option_1(players_score)

# We create a funtion if the player wants to go into the city
def city(players_score):
    print_delay("You enter the city")
    print_delay("you find two mechanic shops")
    print_delay("choose which one you want to enter")
    print_delay("1 = right")
    print_delay("2 = left")
    option_2(players_score)

# We create a function for the second option
def option_2(players_score):
    choice1 = input("Enter your answer (1/2): ")
    if choice1 == "1":
        print_delay("You enter the mechanic shop on your right")
        print_delay("You find a mechanic's kit")
        print_delay("But it is locked and you don't have the key")
        print_delay("Do you want to stay by the box or find the key")
        print_delay("1 = find the key")
        print_delay("2 = stay")
        stay_or_find(players_score)
    elif choice1 == "2":
        print_delay("You enter the mechanic shop on your left")
        print_delay("You find a monster")
        print_delay("He attacks you and you die")
        print_delay("GAME OVER")
    else:
        print_delay("Enter a valid option")
        option_2(players_score)

def stay_or_find(players_score):
    choice2 = input("Enter your answer (1/2): ")
    if choice2 == "1":
        win(players_score)
    elif choice2 == "2":
        if random.randint(0,1) == 0:
            print_delay("You stay by the box")
            print_delay("You starve and die")
            print_delay("GAME OVER")
        elif random.randint(0,1) == 1:
            print_delay("The wolf finds you")
            print_delay("He attacks you and you die")
            print_delay("GAME OVER")
        else:
            print_delay("The atmosphere changes")
            print_delay("Suddenly you find a monster in front of you")
            print_delay("He attacks you")
            print_delay("You die")
            print_delay("GAME OVER")
    else:
        print_delay("Enter a valid option")
        stay_or_find(players_score)

# Create a funtion for winning the game
def win(players_score):
    print_delay("You find the key")
    print_delay("You get out of the city safetly")
    print_delay("You repair you car and get away")
    players_score += 20 
    print_delay(f"Your score is {players_score}")
    print_delay("You WON the game")

def keep_looking(players_score):
    print_delay("You are still looking for a mechanic")
    print_delay("A wolf attacks you")
    print_delay("Do you want to run or to hide")
    print_delay("1 = run")
    print_delay("2 = hide")
    last_option(players_score)

def last_option(players_score):
    run_or_hide = input("Enter your answer (1/2): ")
    if run_or_hide == "1":
        print_delay("The wolf is faster than you")
        print_delay("It catches you and you die")
        print_delay("GAME OVER")
    elif run_or_hide == "2":
        players_score += 10
        print_delay("You get away from the wolf")
        print_delay("You have no option")
        print_delay("You enter the city")
        print_delay(f"Your score is {players_score}")
        city(players_score)
    else:
        print_delay("Please enter a valid option")
        print_delay("Enter your answer (1/2): ")
        last_option(players_score)

game()