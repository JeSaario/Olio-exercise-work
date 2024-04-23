from database import FictionBook, NonFictionBook
import datetime

class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name 
        self.password = password 
        self.loans = []  #List of books currently borrowed by the member

class Library:
    def __init__(self, db):
        self.db = db  #Database object for data persistence
        self.members = {}  #store members with member_id as the key
        self.books = self.db.get_all_books()  #Load books from the database

    def add_book(self, title, author, book_type):
        """
        Add a new book to the library and database if it does not already exist.
        """
        #Check if a book with the same title and author exists
        if any(b.title == title and b.author == author for b in self.books):
            print("Book already exists in the library.")
            return

        #Convert book_type to lowercase for comparison
        book_type_lower = book_type.lower()

        if book_type_lower == "fiction":
            new_book = FictionBook(title, author, "Fiction")
        elif book_type_lower == "non-fiction":
            new_book = NonFictionBook(title, author, "Non-Fiction")
        else:
            print("Invalid book type.")
            return

        self.db.add_book(new_book)
        self.books.append(new_book)
        print("Book added successfully.")

    def return_book(self, title):
        """
        Return a book to the library, marking it as not borrowed.
        """
        for book in self.books:
            if book.title == title and book.borrowed:
                book.return_book()  # This method should mark the book as not borrowed and clear borrower details
                self.db.update_book(book)  # Assuming there is a method to update the book in the database
                print(f"Returned book successfully: {title}")
                return True
        print(f"Book not found or not borrowed: {title}")
        return False

    def add_member(self, member_id, name, password):
        """
        Add a new member to the library's database and dictionary of members.
        """
        self.db.add_member(Member(member_id, name, password))
        self.members[member_id] = Member(member_id, name, password)

    def borrow_book(self, title, member_id):
        """
        Borrow a book with the given title by a member with the given member_id.
        """
        book = next((b for b in self.books if b.title == title and not b.borrowed), None)
        if book:
            member = self.members.get(member_id)
            if member:
                book.borrowed = True
                book.borrower = member
                book.borrowed_date = datetime.datetime.now()  #Set the borrowed date
                return True
        return False

    def return_book(self, title, member_id):
        """
        Return a book with the given title by a member with the given member_id.
        """
        book = next((b for b in self.books if b.title == title and b.borrower and b.borrower.member_id == member_id), None)
        if book and book.borrower.member_id == member_id:
            book.borrowed = False
            book.borrower = None
            book.borrowed_date = None #resetting date
            return True
        return False

    def search_books(self, query=""):
        """
        Search for books in the library based on the given query.
        """
        return self.db.search_books(query)

    def validate_member(self, member_id, password):
        """
        Validate a member's credentials based on their member_id and password.
        """
        member = self.members.get(member_id)
        if member and member.password == password:
            return member
        return None
    
    def get_all_books(self):
        """
        Retrieve all books in the library.
        """
        return self.db.get_all_books()
    
    def view_books(self):
        """
        Display all books in the library with their details.
        """
        print("\nAll Books:")
        for book in self.books:
            if isinstance(book, FictionBook):
                book_type = "Fiction"
            elif isinstance(book, NonFictionBook):
                book_type = "Non-Fiction"
            else:
                book_type = "Unknown Type"

            status = "Borrowed" if book.borrowed else "Available"
            print(f"{book.title} by {book.author} - Type: {book_type} - Status: {status}")

    def view_borrowed_books(self, member_id):
        """
        Display borrowed books for a member along with their borrowing dates.
        """
        print("\nBorrowed Books:")
        borrowed_books = [book for book in self.books if book.borrowed and book.borrower.member_id == member_id]
        for book in borrowed_books:
            print(f"{book.title} by {book.author} - Borrowed Date: {book.borrowed_date}")