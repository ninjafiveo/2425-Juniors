# Functions are essentially a block of code that does nothing until it is called somewhere. 
# DRY! Don’t Repeat Yourself.
# DRY! Don’t Repeat Yourself.
# DRY! Don’t Repeat Yourself.
# How many times have you given the same advice, or directions, or whatever over and over again?
# With functions, you would be able to write the code once and then call it whenever someone needed it.

# "def" is what notifies the code that a function is about to start.
# my_function is the name of the the function below.
# "()" the parenthesis is for the a parameters. The block below has none. ":" the colon lets the code know that the block of code that follows is part of the function.
def my_function ():
    #Any thing that is indented is part of the function. If it is not indented the program reads it as though it is outside the function. Think of Russian nesting dolls, each line needs indented to be a child of the code above.
    print("my function has run")
# In order for the function to run you have to "Call" it. You do that by writing the name of the function with the (). Can't be indented, because that would make it part of the function itself.
my_function()

def npc_greeting():
    print("Hello traveler. Would you like to browse my wares?")

npc_greeting()

# Parameters - Function parameters allow our function to accept data as an input value. We list the parameters a function takes as input between the parentheses of a function ( ).
def player_response(the_response):
    print(the_response)

answer_no = "Nah. I'm good bruh. "
answer_yes = "Oh yes. No Skibidi Ohio stuff tho."
player_response(answer_no)
player_response(answer_yes)

npc_greeting()
player_response(answer_no)

def approach_vendor():
    npc_greeting()
    player_response = input("Enter 1 for yes, 2 for no.")
    player_response = int(player_response)

    if (player_response == 1):
        print("I'd like to buy a Skibidi Toilet.")
    elif (player_response == 2):
        print("Player vanishes like Ninja the Fortnite player streaming on Mixer. To never be heard of again like an off brand Sonic your mom says you have at home.")
    else:
        print("I'm sorry I don't speaka that language, do you have a Vegemite Sandwich?")

approach_vendor()
