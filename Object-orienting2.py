class IOString:
    def __init__(self):
        self.str1 = ""

    def get_str(self):
        self.str1 = input("Enter a string:")
    
    def print_str(self):
        print("Result is", self.str1.upper())

str1 = IOString()
str1.get_str()
str1.print_str()