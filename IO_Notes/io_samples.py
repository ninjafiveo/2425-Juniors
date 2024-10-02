# I/O Notes

#? Write to a text file - Output
# file = open("example.txt", "w")
# file.write("Hello Ninja.")
# file.close()

#? Append a text file - Output
file = open("example.txt", "a")
file.write("Hello Ninja.")
file.write("\n")
file.close()

#? Read from text file.
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

#? Read with open text file. Allows you to read the text file without creating a new variable.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()

# Error Handling - Check out this note: https://docs.google.com/presentation/d/1A9FHHnUcaOGqyQ-PkkqpCiCVS0fI60_YoRKzA8o3XiA/edit#slide=id.g305cf9d5b18_0_80

