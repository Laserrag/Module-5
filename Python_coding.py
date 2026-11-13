class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
        print(f"You have borrowed '{self.title}' by {self.author}.")
    def return_book(self):
        self.is_borrowed = False
        print(f"You have returned '{self.title}' by {self.author} in 7 days.")