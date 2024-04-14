from main import Library, Book, Member
from getpass import getpass

def admin_actions(library):
    while True:
        print("\nAdmin Actions:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Exit to main menu")
        action = input("Choose an action: ")
        if action == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif action == '2':
            name = input("Enter the member name: ")
            member_id = input("Enter the member ID: ")
            password = getpass("Enter a password: ")
            library.add_member(Member(member_id, name, password))
        elif action == '3':
            break

def user_actions(library):
    member_id = input("Enter your member ID: ")
    password = getpass("Enter your password: ")
    member = library.validate_member(member_id, password)
    if member:
        while True:
            print("\nUser Actions:")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. Calculate fines")
            print("4. Exit to main menu")
            action = input("Choose an action: ")
            if action == '1':
                title = input("Enter the book title to borrow: ")
                if not library.borrow_book(title, member.member_id):
                    print("This book is either not available or does not exist.")
            elif action == '2':
                title = input("Enter the book title to return: ")
                if not library.return_book(title, member.member_id):
                    print("You did not borrow this book or it does not exist.")
            elif action == '3':
                print(f"Total fines: ${member.calculate_fines()}")
            elif action == '4':
                break
    else:
        print("Invalid credentials.")

def main():
    library = Library()
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your role or exit: ")
        if choice == '1':
            admin_actions(library)
        elif choice == '2':
            user_actions(library)
        elif choice == '3':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
