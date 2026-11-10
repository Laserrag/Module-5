# Assignment 1
from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("The passed value is:", x)
    
    @abstractmethod
    def task(self):
        print("We are inside Absclass task method.")


class tes_class(Absclass):
    def task(self):
        print("We are inside tes_class task method.")

test = tes_class()
test.print(10)
test.task()

