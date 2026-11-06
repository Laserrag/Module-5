# CLass bank
#__pin attirbute
#method to diplay pin from the class

class Bank:
    def __init__(self, pin =0000):
        self.__pin = pin  # Private attribute
        print(f"Bank account created with PIN: {self.__pin}")

b = Bank(1234)
