# "#" Comments the code - so that humans can read it, but the program ignores it. 
# Uses Comments to communicate what your code does.

# Strings - Strings are words/characters.
first_name = "michael" # Strings have to be inside of " double quotes" or 'single quotes'
# the quotes have to match. You can't have "Hi' a double quote matched with a single quote.
print(first_name)
#Built in functions to strings
print(first_name.capitalize())
the_phrase = "Coding is the most awesome thing to learn ever in this this this this universe and beyond. This statement isn't even that bold."
print(the_phrase.count("this"))
xyz = the_phrase.title()
print(f"istitle {xyz}")

# Side note: the assignment operator & variables. "=" is the assignment operator. It is a command that says the variable name is equal to the value. So first_name = "Michael", is a command telling first_name is "Michael"

# int --> Integers. These are whole numbers: -5, -4, -3, -1, 0, 1, 2, 3, 4... 506,322
user_age = 99
print(user_age)

# floats --> These are numbers with decimal points. 97.6, 101.2
patient_temp = 97.6
print(patient_temp)

# boolean --> True and/or False
w = 100
x = 5
y = 10
z = 10

print(x == y)
print(z == y)
if (x == y):
    print(f"If this prints it's true. x: {x} equals y: {y}")
if (y == z):
    print(f"If this prints it's true. y: {y} equals z: {z}")

# Additional Boolean Operators
# Comparison Operators
# == equal to 
# >= greater than or equal to 
# <= less than or equal to
# < less than
# > greater than
# != not equal to
    
print(w == y)
print(w <= y)
print(w >= y)
print(w < y)
print(w > y)
print(w != y)




