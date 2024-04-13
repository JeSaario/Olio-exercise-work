"""class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.reserve():
            self.borrowed_books.append(book)
            print(f"{book.title} has been successfully borrowed.")
        else:
            print(f"{book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{book.title} has been returned.")
        else:
            print(f"{book.title} is not borrowed by {self.name}.")"""
