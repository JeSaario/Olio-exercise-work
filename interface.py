from library_system import Library
from getpass import getpass


def admin_login():
    #Simple login made for admin
    admin_username = "admin"
    admin_password = "admin"
    username_input = input("Enter admin username: ")
    password_input = getpass("Enter admin password: ")
    if username_input == admin_username and password_input == admin_password:
        return True
    else:
        print("Invalid admin credentials.")
        return False

def admin_menu(library):
    #Displaying the admin menu and handling admin and user input
    if not admin_login():
        return
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new fiction book")
        print("2. Add a new non-fiction book")
        print("3. View all books")
        print("4. Return to main menu")
        choice = input("Choose an action: ")
        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(title, author, "fiction")  # Specify book type as fiction
        elif choice == '2':
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            library.add_book(title, author, "nonfiction")  # Specify book type as non-fiction
        elif choice == '3':
            library.view_books()
        elif choice == '4':
            break


def user_menu(library):
    #Handle user login and display the user menu
    member_id = input("Enter your member ID: ")
    password = getpass("Enter your password: ")
    member = library.validate_member(member_id, password)  #Validate user credentials
    if member:
        while True:
            print("\nUser Menu:")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. View all books")
            print("4. View borrowed books")
            print("5. Exit")
            choice = input("Choose an action: ")
            if choice == '1':
                title = input("Enter the book title to borrow: ")
                #Borrow a book and provide feedback
                if library.borrow_book(title, member_id):
                    print("Book borrowed successfully.")
                else:
                    print("This book is either not available or does not exist.")
            elif choice == '2':
                title = input("Enter the book title to return: ")
                #Return a book and provide feedback
                if library.return_book(title, member_id):
                    print("Book returned successfully.")
                else:
                    print("You did not borrow this book or it does not exist.")
            elif choice == '3':
                library.view_books()  #View all available books
            elif choice == '4':
                print("\nBorrowed Books:")
                #View books borrowed by the user
                borrowed_books = [book for book in library.get_all_books() if book.borrowed and book.borrower.member_id == member_id]
                if borrowed_books:
                    for book in borrowed_books:
                        print(f"{book.title} by {book.author}")
                else:
                    print("You have not borrowed any books yet.")
            elif choice == '5':
                break
    else:
        print("Invalid credentials.")


def main(library):
    #Display main menu and handle user input
    while True:
        print("\nMain Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your role or exit: ")
        if choice == '1':
            admin_menu(library)  #Go to admin menu
        elif choice == '2':
            user_menu(library)  #Go to user menu
        elif choice == '3':
            print("Exiting...")
            break


if __name__ == "__main__":
    from database import Database
    db = Database()
    library = Library(db)
    main(library)

