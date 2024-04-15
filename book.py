import datetime

class Book:
    def __init__(self, title, author):
        """
        Initialize a new Book object with the given title and author.
        """
        self.title = title
        self.author = author
        self.borrowed = False #Initialize book as available
        self.borrowes_date = None #initialixe to none

    def borrow_book(self, member_id):
        if not self.borrowed:
            self.borrowed = True
            self.borrower_id = member_id
            self.borrowed_date = datetime.datetime.now() #Set the borrowed date and time
            return True
        return False

class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def borrow_book(self, member_id):
        #Custom implementation for borrowing a fiction book
        if not self.borrowed:
            self.borrowed = True
            self.borrower_id = member_id
            return True
        return False

class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def borrow_book(self, member_id):
        #Custom implementation for borrowing a non-fiction book
        if not self.borrowed:
            self.borrowed = True
            self.borrower_id = member_id
            return True
        return False