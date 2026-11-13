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

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book1.borrow()
book1.return_book()
print("\n")
book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2.borrow()
book2.return_book()
print("\n")
book3 = Book("The Dragonets of Destiny", "Tui T. Sutherland")
book3.borrow()
book3.return_book()
