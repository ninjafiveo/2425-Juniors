# Create a calculator that has the following functions to perform math on 2 numbers. The 2 numbers should be passed through the function as parameters.
#     * Function for addition
#     * Function for subtraction
#     * Function for multiplication
#     * Function for division
#     * Function for exponent
# The program should ask the user which math function they would like to perform. 
# The program should ask the user for 2 numbers.
# Based on their math function selection, the program should perform that operation on those two numbers and output the result to the console(terminal)
# The program should then ask the user if they would like to perform another math function. If yes, use recursion to start the program over. If no, tell them to have a nice day and that you hope to do math with them again. 

#     * Function for addition
def add(num1, num2):
    return num1 + num2
#     * Function for subtraction
def subtract(num1, num2):
    return num1 - num2
#     * Function for multiplication
def multiply(num1, num2):
    return num1 * num2
#     * Function for division
def divide(num1, num2):
    if(num2 != 0):
        return num1 / num2
    else:
        return "Error: Division by Zero not allowed."
#     * Function for exponent
def exponent(num1, num2):
    return num1 ** num2

def calculator():
    #ask the user which math function they'd like to perform.
    print("Welcome to the Calculator App!")
    print("Please choose a math option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")

    # Get the user's choice
    choice = input("Enter the number of the operation you want to perform (1-5): ")
    num1 = float(input("Please enter number 1: "))
    num2 = float(input("Please enter number 2: "))

    # Perform the math... use the right function/operation below
    if(choice == "1"):
        result = add(num1, num2)
        print("The result of adding ", {num1}, " and ", {num2}, " is ",{result}, ".")
    elif(choice == "2"):
        result = subtract(num1, num2)
        print(f"The result of subtracting {num1} and {num2} is {result}.")
    elif(choice == "3"):
        result = multiply(num1, num2)
        print(f"The result of multiplying {num1} and {num2} is {result}.")
    elif(choice == "4"):
        result = divide(num1, num2)
        print(f"The result of dividing {num1} and {num2} is {result}.")
    elif(choice == "5"):
        result = exponent(num1, num2)
        print(f"The result of power of {num1} and {num2} is {result}.")
    else:
        print("Invalid Choice. Try Again. ")
        calculator()
        
    # Ask user if they want to keep doing math.
    again = input("Do more math? y/n: ")
    if(again == "y"):
        calculator()
    else:
        print("have a great day.")

calculator()
