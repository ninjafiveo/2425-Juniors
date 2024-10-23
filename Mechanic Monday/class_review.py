# What is a class?
# Blueprint - Its a preplanned layout to create an object.
# What can an object have? Attributes (Variables), Methods (These are functions inside of a class), Identity

# Create the class, the blueprint to creat future objects. 
class Dinosaur:
    # Make the constructor
    def __init__(self, name, species, diet):
        self.name = name # Dinos name
        self.species = species # Dino's Speacies
        self.diet = diet # Dino's diet
    
    # Create Methods - Actions that the Dino's can do.
    def rawr(self):
        print(f"{self.name} let's out a mighty raaaaawwr.")

    # Pass an argument through the parameter ()
    def eat(self, food):
        if food == self.diet:
            print(f"{self.name} eats {food}... Mmm... Delish. Uncle Roger agrees.")
        else:
            print(f"{self.name} doesn't eat {food}")
    

rex = Dinosaur("Steve", "Tyrannosaurus Rex", "meat")

spike = Dinosaur("Spike", "Stegosaurus", "plants")
george = Dinosaur("George", "Pterodactyl", "everything")

# print(rex.name)

rex.rawr()
rex.eat("plants")
rex.eat("meat")




