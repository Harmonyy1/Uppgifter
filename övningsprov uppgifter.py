#3

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
    



        