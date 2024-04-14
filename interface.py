from library_system import Library
from getpass import getpass


def admin_menu(library):
    #Displaying the admin menu and handling user input
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. View all books")
        print("4. Return to main menu")
        choice = input("Choose an action: ")
        if choice == '1':
            #Getting book details and adding a new book to the library
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(title, author)
        elif choice == '2':
            #Getting member details and adding a new member to the library
            member_id = input("Enter the member ID: ")
            name = input("Enter the member name: ")
            password = getpass("Enter a password: ")
            library.add_member(member_id, name, password)
        elif choice == '3':
            #Displaying all books in the library
            books = library.search_books()
            for book in books:
                print(f"{book.title} by {book.author} - {'Borrowed' if book.borrowed else 'Available'}")
        elif choice == '4':
            break

def user_menu(library):
    #Handling user login and displaying the user menu
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
                #book borrow
                title = input("Enter the book title to borrow: ")
                if library.borrow_book(title, member_id):
                    print("Book borrowed successfully.")
                else:
                    print("This book is either not available or does not exist.")
            elif choice == '2':
                #book return
                title = input("Enter the book title to return: ")
                if library.return_book(title, member_id):
                    print("Book returned successfully.")
                else:
                    print("You did not borrow this book or it does not exist.")
            elif choice == '3':
                break
    else:
        print("Invalid credentials.")

def main(library):
    #Displaying the main menu and handling user input
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your role or exit: ")
        if choice == '1':
            admin_menu(library)
        elif choice == '2':
            user_menu(library)
        elif choice == '3':
            print("Exiting...")
            break

if __name__ == "__main__":
    from database import Database
    db = Database()
    library = Library(db)
    main(library)