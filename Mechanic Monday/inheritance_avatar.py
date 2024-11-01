class Bender:
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def bend(self):
        return f"{self.name} is bending {self.element}."
    
class FireBender(Bender):
    def __init__(self, name):
        super().__init__(name, "Fire")

class EarthBender(Bender):
    def __init__(self, name):
        super().__init__(name, "Earth")

zuko = FireBender("Zuko")
toph = EarthBender("Toph")

print(zuko.bend())
print(toph.bend())