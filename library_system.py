import datetime
from database import Book

class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name 
        self.password = password 
        self.loans = []  #List of books currently borrowed by the member

    '''def calculate_fines(self):
        today = datetime.now()  #Get the current date and time
        fine_total = 0 
        for loan in self.loans:
            if loan.due_date < today:
                overdue_days = (today - loan.due_date).days  #Calculate the number of days the book is overdue
                fine_total += 1 * overdue_days  #Fine is 1€/day
        return fine_total'''

class Library:
    def __init__(self, db):
        self.db = db  #Database object for data persistence
        self.members = {}  #store members with member_id as the key
        self.books = self.db.get_all_books()  #Load books from the database

    def add_book(self, title, author):
        """
        Add a new book to the library and database if it does not already exist.
        """
        new_book = Book(title, author)
        if not any(b.title == new_book.title for b in self.books):
            self.db.add_book(new_book)  # Add to database
            self.books.append(new_book)  # Add to library


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
        book = next((b for b in self.members[member_id].loans if b.title == title), None)  #Find the book with the given title in the member's list of loans
        if book:
            book.borrowed = False  
            self.members[member_id].loans.remove(book)  #Remove the book from the member's list of loans
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

    def view_books(self):
        for book in self.books:
            if not book.borrowed:
                status = "Available"
            else:
                status = f"Borrowed by: {book.borrower.name}" if book.borrower else "Borrowed (Unknown)"
            print(f"{book.title} by {book.author} - {status}")