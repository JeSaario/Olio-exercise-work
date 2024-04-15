class Book:
    def __init__(self, title, author):
        """
        Initialize a new Book object with the given title and author.
        """
        self.title = title
        self.author = author
        self.borrowed = False # Initialize book as available
        #self.due_date = None

    """def borrow_book(self):
        if not self.borrowed:
            self.borrowed = True
            return True
        return False

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return True 
        return False"""

class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)  #Call constructor of parent class to initialize title and author
        self.genre = genre

class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

class Database:
    def __init__(self):
        """
        Initialize a new Database object with empty lists for books and members.
        """
        self.books = []
        self.members = {}

    def add_book(self, book):
        """
        Add a new book to the database if it does not already exist.
        """
        if not any(b.title == book.title for b in self.books):
            self.books.append(book)

    def add_member(self, member):
        """
        Add a new member to the database.
        """
        self.members[member.member_id] = member

    def borrow_book(self, title, member_id):
        """
        Borrow a book with the given title by a member with the given member_id.
        """
        #Make sure to use a generator to find the book
        book = next((b for b in self.books if b.title == title and not b.borrowed), None)
        if book and member_id in self.members:
            member = self.members[member_id]
            book.borrowed = True
            book.borrower = member
            return True
        return False

    def return_book(self, title, member_id):
        """
        Return a book with the given title by a member with the given member_id.
        """
        book = next((b for b in self.books if b.title == title and b.borrower and b.borrower.member_id == member_id), None)
        if book:
            book.borrowed = False
            book.borrower = None
            return True
        return False

    def search_books(self, query=""):
        """
        Search for books in the database with the given query.
        """
        return [book for book in self.books if query.lower() in book.title.lower()]

    def validate_member(self, member_id, password):
        """
        Validate a member's credentials with the given member_id and password.
        """
        member = self.members.get(member_id)
        if member and member.password == password:
            return member
        return None
        
    def get_all_books(self):
        """
        Retrieve all books stored in the database.
        """
        return list(set(self.books))  # Use a set to remove duplicates and then convert back to a list