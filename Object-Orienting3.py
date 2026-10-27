class employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Distructor called")

def create_object():
    print("Making object")
    obj = employee()
    print("Function end!")
    return obj

print("Calling create object")
obj = create_object
print("Program end")