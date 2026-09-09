class Animal:

    def sound(self):
        print("sound....")

class Dog(Animal):
    def sound(self):
        print("Bark...")

class Cat(Animal):

    def sound(self):
        print("Meow")

animals = [Dog(),Cat()]
for i in animals:
    i.sound()
