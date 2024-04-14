from datetime import datetime, timedelta
from getpass import getpass

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

    def display_books(self):
        print("\nCatalog of Books:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def display_members(self):
        print("\nList of Members:")
        for member_id, member in self.members.items():
            print(f"Member ID: {member_id}, Name: {member.name}")

    def borrow_book(self, title, member_id):
        member = self.members.get(member_id)
        if member:
            book = next((b for b in self.books if b.title == title and not b.borrowed), None)
            if book:
                book.borrowed = True
                book.borrower = member
                book.due_date = datetime.now() + timedelta(days=14)  # Default due date of 14 days
                member.borrowed_books.append(book)
                return True
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
                return True
        return False

    def validate_member(self, member_id, password):
        member = self.members.get(member_id)
        if member and member.password == password:
            return member
        return None

def admin_menu(library):
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. View catalog of books")
        print("4. View all members")
        print("5. Return to main menu")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif choice == '2':
            name = input("Enter the member name: ")
            member_id = input("Enter the member ID: ")
            password = getpass("Enter a password: ")
            library.add_member(Member(member_id, name, password))
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            library.display_members()
        elif choice == '5':
            break

def user_menu(library):
    member = None
    while not member:
        member_id = input("Enter your member ID: ")
        password = getpass("Enter your password: ")
        member = library.validate_member(member_id, password)
        if not member:
            print("Invalid credentials. Try again.")
    
    while True:
        print("\nUser Menu:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View borrowed books")
        print("4. Check fines")
        print("5. Logout")
        choice = input("Choose an action: ")
        if choice == '1':
            title = input("Enter the book title to borrow: ")
            if not library.borrow_book(title, member.member_id):
                print("This book is either not available or does not exist.")
        elif choice == '2':
            title = input("Enter the book title to return: ")
            if not library.return_book(title, member.member_id):
                print("You did not borrow this book or it does not exist.")
        elif choice == '3':
            library.display_borrowed_books(member.member_id)
        elif choice == '4':
            print(f"Total fines: ${member.calculate_fines()}")
        elif choice == '5':
            break

def main():
    library = Library()
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role = input("Choose 1 for Admin, 2 for User, 3 to Exit: ")
        if role == '1':
            admin_menu(library)
        elif role == '2':
            user_menu(library)
        elif role == '3':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
