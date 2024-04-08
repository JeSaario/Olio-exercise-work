from book import Book
from catalog import Catalog
from member import Member
from reference_book import ReferenceBook

def main():
    catalog = Catalog()

    # Adding books
    book1 = Book("Python 101", "Author A", "123456")
    book2 = ReferenceBook("Advanced Python", "Author B", "789012", "Programming")
    catalog.add_book(book1)
    catalog.add_book(book2)

    # Creating a member
    member = Member("John Doe")

    # Borrowing a book
    member.borrow_book(book1)
    catalog.display_available_books()

    # Returning a book
    member.return_book(book1)
    catalog.display_available_books()

if __name__ == "__main__":
    main()
