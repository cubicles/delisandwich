# delisandwich cli
#
# Self-study, introspective project to build a full end to end python project
# that helps deepen the understanding of a project lifecycle
#
# Starts with a basic command line interface (cli) that allows the user to
# create a deli sandwich order. The project is incomplete so that one can
# clone the repo or branch new features in order to train themselves on
# the project lifecycle
#
# At its full projected level it will include a dockerfile to containerize
# the project, requirements, setup, tests, CI/CD and Maturin bindings
# to optimize the project for performance

# mock a basic cli greeting message to the user

import os
import sys

def cli_greeting_menu():
    ''' cli_greeting_menu
        -----------------
        Displays a welcome message to the user with various options to choose
        from. The user can create a new sandwich order or view an existing 
        sandwich
    '''

    # print a greeting message to the user  
    print("Welcome to the delisandwich CLI!")
    print("--------------------------------")
    # I want an ascci art of a sandwich here
    ascii_art = r"""
     _      _ _                     _          _      _     
    | |    | (_)                   | |        (_)    | |    
  __| | ___| |_ ___  __ _ _ __   __| |_      ___  ___| |__  
 / _` |/ _ \ | / __|/ _` | '_ \ / _` \ \ /\ / / |/ __| '_ \ 
| (_| |  __/ | \__ \ (_| | | | | (_| |\ V  V /| | (__| | | |
 \__,_|\___|_|_|___/\__,_|_| |_|\__,_| \_/\_/ |_|\___|_| |_|
                                                            
    """
    print(ascii_art)
    # Display a menu of options to the user
    print("--------------------------------")
    print("Train yourself on the arts of data manipulation by creating delicious sandwiches!")
    print("Please select from the following options:")
    print("1. Select a challenge from the menu")
    print("2. View a random challenge")
    print("3. Exit")
    print("--------------------------------")
    # keep the program running until the user exits
    while True:
        # get the user's input
        user_input = input("Please enter your choice: ")
        # check if the user wants to create a new sandwich order
        if user_input == '1':
            print("You selected a challenge")
            # create a new sandwich order
            # this is a placeholder for future functionality
            print("This feature is not yet implemented")
        # check if the user wants to view an existing sandwich order
        elif user_input == '2':
            print("You selected a random challenge")
            # view an existing sandwich order
            # this is a placeholder for future functionality
            print("This feature is not yet implemented")
        # check if the user wants to exit the program
        elif user_input == '3':
            print("You selected to exit the program")
            # exit the program
            sys.exit()
        # handle invalid input from the user
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == '__main__':
    cli_greeting_menu()
