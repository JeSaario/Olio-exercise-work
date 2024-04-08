class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            return True
        return False

    def return_book(self):
        if self.reserved:
            self.reserved = False
            return True
        return False
