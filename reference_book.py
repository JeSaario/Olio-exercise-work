from book import Book

class ReferenceBook(Book):
    def __init__(self, title, author, isbn, subject):
        super().__init__(title, author, isbn)
        self.subject = subject

    # Example of polymorphism: override the reserve method
    def reserve(self):
        return False  # Reference books cannot be reserved
