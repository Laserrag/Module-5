class computer:
    def __init__(self):
        self.__maxpricae = 9000
    def sell(self):
        print("Selling Price: {}".format(self.__maxpricae))
    def setMaxPrice(self, price):
        self.__maxpricae = price

c = computer()
c.sell()
c.setMaxPrice(10000)
c.sell()

c.__maxpricae = 20000
c.sell()