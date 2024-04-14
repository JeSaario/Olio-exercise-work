from main import Library, Book, Member

library = Library()

def add_new_book():
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    year = input("Enter the year of the new book: ")
    book = Book(title, author, year)
    library.add_book(book)
    print("Book added successfully.")


def add_new_member():
    name = input("Enter the name of the new member: ")
    member_id = input("Enter the ID of the new member: ")
    password = input("Enter a password for the new member: ")
    member = Member(member_id, name, password)
    library.add_member(member)
    print(f"Member added successfully.")


def main():
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            add_new_member()
        elif choice == '3':
            print("Exiting admin interface...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()