class Family_Member:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm
    def show_traits(self):
        print(f"Eye Color: {self.eye_color}")
        print(f"Height: {self.height_cm} cm")

class Kid(Family_Member):
    def __init__(self, name, age, eye_color, height_cm):
        super().__init__(eye_color, height_cm)
        self.name = name
        self.age = age
    def show_traits(self):
        super().show_traits()
        print(f"Name: {self.name}")
        print(f"Age: {self.age} years")
    def favourite_hobby(self, hobby):
        print(f"{self.name}'s favourite hobby is {hobby}.")

child = Kid("Alice", 10, "Blue", 140)
child.show_traits()
child.favourite_hobby("playing with dolls")

issubclass(Kid, Family_Member)  # Returns True

#Assignment:
#Animal class
#Eat method print animal eats food
#dog child class
#Bark method print dog bark
#Dog object call dog

class Animal:
    def eat(self):
        print("Animal eats food.")

class dog(Animal):
    def bark(self):
        super().eat()
        print("Dog Barks")

Dog = dog()
Dog.bark()
Dog.eat()