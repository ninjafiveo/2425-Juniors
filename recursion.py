# Below is an example of recursion.

def my_recursion():
    choice = input("Would you like to play a game, y or n: ")
    choice = choice.lower()
    if(choice == "y"):
        my_recursion()
    elif(choice == "n"):
        print("Have a lovely day.")
    else:
        print("No idea what you said. Please use 'y' or 'n' only.")
        my_recursion()

my_recursion()