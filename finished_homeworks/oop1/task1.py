# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

class Animals:
    """
    Parent class, should have eat, sleep
    """

    def __init__(self, name, years):
        self.name = name
        self.years = years

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")


class Lion(Animals):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def eat(self):
        print(f"I'm {self.name} and I'm eating zebra")

    def run(self):
        print("RUUUUUN!")


class Zebra(Lion):

    def __init__(self, name, years):
        super().__init__(name, years)


animal = Lion("Lion", "2")
animal.eat()

animal1 = Zebra("Zebra", "3")
animal1.eat()
print(isinstance(animal, Animals))
print(isinstance(animal1, Animals))


class Human:

    def eat(self):
        print(f"I'm eat")

    def sleep(self):
        print("I'm sleeping")

    def study(self):
        print("I'm studying!")

    def work(self):
        print("I'm working!")


class Centaur(Animals, Human):
    def go(self):
        print("I'm going!!")


centaur = Centaur("cent", 15)
centaur.eat()
centaur.work()
centaur.go()
print(isinstance(centaur, Animals))




