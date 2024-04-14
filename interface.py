# Importing necessary libraries
# from library_system import Library # Importing the Library class from the library_system module
# from getpass import getpass # Importing the getpass function to hide password input

def admin_menu(library):
    # Displaying the admin menu and handling user input
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. View all books")
        print("4. Return to main menu")
        choice = input("Choose an action: ")
        if choice == '1':
            # Getting book details and adding a new book to the library
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(title, author)
        elif choice == '2':
            # Getting member details and adding a new member to the library
            member_id = input("Enter the member ID: ")
            name = input("Enter the member name: ")
            password = getpass("Enter a password: ")
            library.add_member(member_id, name, password)
        elif choice == '3':
            # Displaying all books in the library
            books = library.search_books()
            for book in books:
                print(f"{book.title} by {book.author} - {'Borrowed' if book.borrowed else 'Available'}")
        elif choice == '4':
            # Exiting the admin menu
            break

def user_menu(library):
    # Handling user login and displaying the user menu
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
                # Handling book borrowing
                title = input("Enter the book title to borrow: ")
                if library.borrow_book(title, member_id):
                    print("Book borrowed successfully.")
                else:
                    print("This book is either not available or does not exist.")
            elif choice == '2':
                # Handling book returning
                title = input("Enter the book title to return: ")
                if library.return_book(title, member_id):
                    print("Book returned successfully.")
                else:
                    print("You did not borrow this book or it does not exist.")
            elif choice == '3':
                # Exiting the user menu
                break
    else:
        # Displaying an error message for invalid credentials
        print("Invalid credentials.")

def main(library):
    # Displaying the main menu and handling user input
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your role or exit: ")
        if choice == '1':
            # Calling the admin_menu function
            admin_menu(library)
        elif choice == '2':
            # Calling the user_menu function
            user_menu(library)
        elif choice == '3':
            # Exiting the program
            print("Exiting...")
            break

if __name__ == "__main__":
    # Importing the Database class from the database module
    from database import Database
    # Initializing the Database object
    db = Database()
    # Initializing the Library object with the Database object
    library = Library(db)
    # Calling the main function with the Library object
    main(library)