from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
        self.borrower = None
        self.due_date = None

class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.password = password

class Database:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        if not any(b.title == book.title for b in self.books):
            self.books.append(book)

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, title, member_id):
        # Make sure to use a generator to find the book
        book = next((b for b in self.books if b.title == title and not b.borrowed), None)
        if book and member_id in self.members:
            member = self.members[member_id]
            book.borrowed = True
            book.borrower = member
            return True
        return False

    def return_book(self, title, member_id):
        book = next((b for b in self.books if b.title == title and b.borrower and b.borrower.member_id == member_id), None)
        if book:
            book.borrowed = False
            book.borrower = None
            return True
        return False

    def search_books(self, query=""):
        return [book for book in self.books if query.lower() in book.title.lower()]

    def validate_member(self, member_id, password):
        member = self.members.get(member_id)
        if member and member.password == password:
            return member
        return None