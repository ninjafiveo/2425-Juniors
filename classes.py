class Dog:

    #Class Attribute (Shared by all instances)
    species = "Canis lupu familiaris"
    
    #! Constructor: Initializes instance of attribute
    #* Think of Bob the Builder with Blueprints ready to make the house.
    def __init__(self, name, age, breed, fur_type, sheds): #2 underscores before and after the init = dunder...Double Underline 
        self.name = name            # Instance Attribute
        self.age = age              # Instance Attribute
        self.breed = breed          # Instance Attribute
        self.fur_type = fur_type    # Instance Attribute
        self.sheds = sheds          # Instance Attribute
    

    #! Method: Instance method (AKA Functions inside a class)
    #? Method: Describe Doggo
    def description (self):
        return f"{self.name} is {self.age} years old. {self.name} is a {self.breed}."
    
    #? Method: Dog to Human Years Conversion
    def age_in_human_years(self):
        human_age = self.age * 7
        return f"{self.name} is {human_age} years old in human years."
    
#! Create an instance(Object) of the Dog Class
dog1 = Dog("Mozzy", 5, "Maltipoo", "Hair", False)
dog2 = Dog("Chloe", 11, "Pit", "Fur", True)

#! Access Class Attributes
print(f"{dog1.name} belongs to the species: {dog1.species}")

#! Access Instance attributes and methods
print(dog1.description())
print(f"{dog1.name} is {dog1.age_in_human_years()}")

print(dog2.description())
print(f"{dog2.name} is {dog2.age_in_human_years()}")

