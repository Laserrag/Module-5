#Assignment 2:
#Abs class animal
#abs eat method 
#dawg class inherits animal class and implements eat method and cat class inherits animal class and eats like a queen(milk)

from abc import ABC, abstractmethod

class animal(ABC):

    @abstractmethod
    def eat(self):
        print("Animal is eating")

class dawg(animal):
    def eat(self):
        super().eat()
        print("dawg is eating messly with no manners.")

class cat(animal):
    def eat(self):
        super().eat()
        print("Cat is eating and drinking milk like a queen.")

animal1 = dawg()
animal1.eat()
animal2 = cat()
animal2.eat()