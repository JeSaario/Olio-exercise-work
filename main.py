from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False
        self.borrower = None
        self.due_date = None


class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.password = password
        self.borrowed_books = []


    def calculate_fines(self):
        today = datetime.now()
        fine_total = 0
        for book in self.borrowed_books:
            if book.due_date and book.due_date < today:
                overdue_days = (today - book.due_date).days
                fine_total += 5 * overdue_days  # Assuming $5 fine per overdue day
        return fine_total
    

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member added: {member.name}")

    def borrow_book(self, title, member_id):
        member = self.members.get(member_id)
        if member:
            book = next((b for b in self.books if b.title == title and not b.borrowed), None)
            if book:
                book.borrowed = True
                book.borrower = member
                book.due_date = datetime.now() + timedelta(days=14)  # Default due date of 14 days
                member.borrowed_books.append(book)
                print(f"{member.name} borrowed {book.title}")
                return True
        print("Borrowing failed.")
        return False


    def return_book(self, title, member_id):
        member = self.members.get(member_id)
        if member:
            book = next((b for b in member.borrowed_books if b.title == title), None)
            if book:
                book.borrowed = False
                book.borrower = None
                book.due_date = None
                member.borrowed_books.remove(book)
                print(f"{book.title} returned.")
                return True
        print("Return failed.")
        return False
    
    def validate_member(self, member_id, password):
        member = self.members.get(member_id)
        if member and member.password == password:
            return member
        return None  
    
    def display_borrowed_books(self, member_id):
        member = self.members.get(member_id)
        if member:
            for book in member.borrowed_books:
                print(f"{book.title} due on {book.due_date.strftime('%Y-%m-%d')}")