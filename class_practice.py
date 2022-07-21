#Exploring class creation
class Cat:
    def __init__(self, name):
        self.name = name

first_cat = Cat("Felix")
print(first_cat.name)

second_cat = Cat("Garfield")
print(second_cat.name)

class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def bark(self):
        return self.sound + ' ' + self.sound

first_dog = Dog("Fido","Brown","woof!")
print(first_dog.name)
print(first_dog.color)
first_dog.bark()