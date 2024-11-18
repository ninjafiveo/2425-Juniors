# Lists are ordered, mutable sequence of items. 
# Dictionaries - are unordered collections that store data as key-value pairs.

#Example
# Lists
fruits= ['apple', 'strawberry', 'banana', 'kiwi']
print(fruits)

# Dictionary
fruit_colors = {'apple':'red', 'banana':'green', 'kiwi':'golden'}
print(fruit_colors)

# Built in List Methods - append(), remove(), sort(), pop() and insert() 

# Add an item
fruits.append('orange')
print(fruits)

# Remove an item
fruits.remove('banana')
print(fruits)

# Sort List
fruits.sort()
print(fruits)

# Nested Lists - Lists of lists. This allows for "Multi-dimensional" data storage.
matrix = [[1, 2, 3],[ 4, 5 , 6],[ 7, 8, 9]]
# output
print(matrix[1][1])
print(matrix[0][2])
print(matrix[2][0])

# Dictionary Methods
# Accessing keys and values
keys = fruit_colors.keys()
values = fruit_colors.values()
print(keys)
print(values)

# Update Dictionary
fruit_colors['apple'] = 'green'
print(values)

# Using get() to handle missing keys
print(fruit_colors.get('orange', 'Not Found'))

fruit_colors['orange'] = 'blood orange'
print(fruit_colors.get('orange', 'Not Found'))

fruit_colors.update({'grapes':'purple'}) 
print(fruit_colors)