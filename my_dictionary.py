# Examples of a Dictionary
student_grades = {
   "Alice": 90,
   "Bob": 85,
   "Charlie": 92
}
print("This is everything in the dictionary: ", student_grades)
# student_1 = student_grades["Alice"]
# print("Student: ", student_1)  # Output: 90
# current_grade = input("Enter the name of the student you are searching for: ")
# print(f"The grade for {current_grade} is: {student_grades[current_grade]}")
# print(student_grades) # Outputs: {'Alice': 90, 'Bob': 87, 'Charlie': 92, 'David': 88}

student_grades["David"] = 88 #! Adding data
student_grades["Bob"] = 87 #! Updating Data - Typos cause major problems by adding new people.
print("This is the updated Dictionary: ", student_grades) # Outputs: {'Alice': 90, 'Bob': 87, 'Charlie': 92, 'David': 88}

del student_grades["Charlie"] # Example using del
student_grades.pop("Bob") # Example using pop()
print(student_grades) # Prints {'Alice': 90, 'David': 88}

if "Alice" in student_grades: # Checking for a Key
    print("Alice's grade is", student_grades["Alice"])

# Add the people back in:
student_grades["David"] = 88
student_grades["Bob"] = 87 
student_grades["Bob"] = 33 
student_grades["Charlie"] = 93

for name, grade in student_grades.items(): # For loop to check data in dictionary
    print(name, "has a grade of", grade)
