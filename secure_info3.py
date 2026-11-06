class point:
    def __init__(self, x = 10, y = 20):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = point(2,3)
print(p1)
