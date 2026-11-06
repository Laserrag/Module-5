class my_class:
    __private_variable = 29
    def __private_method(self):
        print("This is a private method")
    def hello(self):
        print("Hello, my class has", my_class.__private_variable, "students")

a = my_class()
a.hello()
a.__private_method()

# Assignment