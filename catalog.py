from database import Database

class Catalog:
    def __init__(self):
        """
        Initialize the Catalog class with a Database object.
        """
        self.database = Database()

    def add_book(self, title, author, year):
        """
        Add a book to the database with the given title, author, and year.

        :param title: The title of the book.
        :param author: The author of the book.
        :param year: The year the book was published.
        """
        self.database.add_book(title, author, year)

    def find_books_by_title(self, title):
        """
        Find books in the database with a title containing the given string.

        :param title: The title to search for in the database.
        :return: A list of books with titles containing the given string.
        """
        found_books = [book for book in self.database.get_books() if title.lower() in book['title'].lower()]
        return found_books