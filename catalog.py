from database import Database

class Catalog:
    def __init__(self):
        self.database = Database()

    def add_book(self, title, author, year):
        self.database.add_book(title, author, year)

    def find_books_by_title(self, title):
        found_books = [book for book in self.database.get_books() if title.lower() in book['title'].lower()]
        return found_books
