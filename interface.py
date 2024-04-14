from main import Library, Book, Member
from getpass import getpass

library = Library()  # Assumes all data initialization is handled in main.py

def admin_actions():
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Exit")
        choice = input("Choose an action: ")
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
            break

def user_actions():
    member_id = input("Enter your member ID: ")
    password = getpass("Enter your password: ")
    member = library.validate_member(member_id, password)
    if member:
        while True:
            print("\nUser Menu:")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. Exit")
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
                break
    else:
        print("Invalid credentials.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role = input("Enter your role or exit: ")
        if role == '1':
            admin_actions()
        elif role == '2':
            user_actions()
        elif role == '3':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
