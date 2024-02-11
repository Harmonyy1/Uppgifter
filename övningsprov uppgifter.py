#3
"""
class Animal():

    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Woof")
    
class Cat(Animal):
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

dog = Dog()

cat = Cat()

make_sound(dog)
make_sound(cat)
"""   


#4
"""
class Skolklass:
    def __init__(self, namn, antal_elever):
        self.namn = namn
        self.antal_elever = antal_elever


enKlass = Skolklass("TE20", 32)

print(enKlass.namn)
print(enKlass.antal_elever)
print(type(enKlass))
print(type(enKlass.namn))
print(type(enKlass.antal_elever))
"""


#5              GÖR DENNA SENARE!!!
"""
class Skolklass:
    def __init__(self, namn, antalElever):
        self.namn = namn
        self.antal_elever = antalElever

Klasser = []
while True:
    namn = input("Ange klassens namn: (Avsluta med #) ")
    if namn == "#":
        break

    antalElever = int(input("Ange antal elever: "))


    Klasser.append(Skolklass(namn, antalElever))

print("Klass".ljust(7), "Antal elever".ljust(15))
for klass in Klasser:
    print((klass.namn).ljust(7), str(klass.antalElever).ljust(15))
"""