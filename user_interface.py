# user_interface.py
from main import Library
from getpass import getpass

library = Library()

def borrow_book(member):
    title = input("Enter the title of the book to borrow: ")
    if library.borrow_book(title, member.member_id):
        print("Book borrowed successfully.")
    else:
        print("This book is either not available or does not exist.")

def return_book(member):
    title = input("Enter the title of the book to return: ")
    if library.return_book(title, member.member_id):
        print("Book returned successfully.")
    else:
        print("You did not borrow this book or it does not exist.")

def view_borrowed_books(member):
    print("Your borrowed books:")
    library.display_borrowed_books(member.member_id)

def check_fines(member):
    print(f"Total fines: ${member.calculate_fines()}")

def user_login():
    while True:
        member_id = input("Enter your member ID: ")
        password = getpass("Enter your password: ")
        member = library.validate_member(member_id, password)
        if member:
            print(f"Welcome, {member.name}!")
            return member
        else:
            print("Invalid ID or password. Please try again.")

def main():
    print("Welcome to the Library User Interface")
    logged_in_member = user_login()
    while True:
        print("\nUser Menu:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. View borrowed books")
        print("4. Check fines")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            borrow_book(logged_in_member)
        elif choice == '2':
            return_book(logged_in_member)
        elif choice == '3':
            view_borrowed_books(logged_in_member)
        elif choice == '4':
            check_fines(logged_in_member)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
