# Create the Dictionary
hogwarts_houses = {"Harry":"Gryffindor", "Hermione":"Gryffindor", "Draco":"Slytherin", "Cedric":"Hufflepuff", "Cho":"Ravenclaw" }
#! The Key = Harry
#! The Value = Gryffindor

# Get value with the default. I.e Asks for the value to the key. If it is unknown it will print, unknown.
# print(hogwarts_houses.get("Harry", "Unknown"))
# print(hogwarts_houses.get("Luna", "Unknown"))

# Get Keys and Values
# print(hogwarts_houses.keys())
# print(hogwarts_houses.values())
# Get Everything
# print(hogwarts_houses)

# Get Items (key-value pairs)
# print(hogwarts_houses.items())

# Pop and popitem
# print("Before pop: ", hogwarts_houses)
# print(hogwarts_houses.pop("Draco"))
# print("After pop Draco: ", hogwarts_houses)
# print(hogwarts_houses.popitem())
# print("After popping last item: ",hogwarts_houses)

# Clear the dictionary
print(hogwarts_houses)
hogwarts_houses.clear()
print(hogwarts_houses)

# Update and copy
hogwarts_houses = {"Harry":"Gryffindor"}
new_characters ={"Luna":"Ravenclaw", "Neville":"Gryffindor"}
hogwarts_houses.update(new_characters)
print(hogwarts_houses)
copy_of_houses = hogwarts_houses.copy()
print(copy_of_houses)
print(hogwarts_houses.popitem())
print("After popping last item: ",hogwarts_houses)
print(copy_of_houses)

#Set Default value for new key:
hogwarts_houses.setdefault("Draco", "Slytherin")
print(hogwarts_houses)