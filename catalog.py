"""from book import Book

class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_available_books(self):
        available_books = [book.title for book in self.books if not book.reserved]
        print("Available books:", ", ".join(available_books))"""
