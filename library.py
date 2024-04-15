from book import FictionBook, NonFictionBook
from member import Member

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

        self.db.add_book(new_book)  #Add to database
        self.books.append(new_book)  #Add to library
        print("Book added successfully.")


    def add_member(self, member_id, name, password):
        self.db.add_member(Member(member_id, name, password))  #Add a new member to the database
        self.members[member_id] = Member(member_id, name, password)  #Add the new member to the library's dictionary of members
    

    def borrow_book(self, title, member_id):
        """
        Borrow a book with the given title by a member with the given member_id.
        """
        book = next((b for b in self.books if b.title == title and not b.borrowed), None)
        if book:
            member = self.members.get(member_id)
            if member:
                book.borrowed = True
                book.borrower = member  #Assign the borrower to the book
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
            return True
        return False

    def search_books(self, query=""):
        return self.db.search_books(query)  #Search for books in the database based on the given query

    def validate_member(self, member_id, password):
        member = self.members.get(member_id)
        if member and member.password == password:  #Check if the member exists and the password is correct
            return member
        return None
    
    def get_all_books(self): 
        return self.db.get_all_books()  #Retrieve all books in the library
    
    def add_book(self, title, author, book_type):
        """
        Add a new book to the library and database if it does not already exist.
        """
        #Check if a book with the same title and author exists
        if any(b.title == title and b.author == author for b in self.books):
            print("Book already exists in the library.")
            return

        if book_type.lower() == "fiction": #Convert book_type to lowercase for comparison
            new_book = FictionBook(title, author, "Fiction")
        elif book_type.lower() == "non-fiction":
            new_book = NonFictionBook(title, author, "Non-Fiction")
        else:
            print("Invalid book type.")
            return

        self.db.add_book(new_book)  #Add to database
        self.books.append(new_book)  #Add to library
        print("Book added successfully.")

    def view_books(self):
        """
        Display all books in the library with their details.
        """
        print("\nAll Books:")
        for book in self.books:  #Iterate through each book in the library
            if isinstance(book, FictionBook):  #Check if the book is fiction
                book_type = "Fiction"
            elif isinstance(book, NonFictionBook):
                book_type = "Non-Fiction"
            else:
                book_type = "Unknown Type"  #Handle unknown book types

            status = "Borrowed" if book.borrowed else "Available"  #Check book availability
            print(f"{book.title} by {book.author} - Type: {book_type} - Status: {status}")

  #Check if the book is borrowed
            if book.borrowed:
                availability = f"Borrowed by {book.borrower.name}"
            else:
                availability = "Available"

            print(f"{book.title} by {book.author} - Type: {book_type} - Status: {availability}")