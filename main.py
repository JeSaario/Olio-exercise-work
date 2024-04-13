from datetime import datetime, timedelta
from library_system import Book, Member, Library

#Create library
library = Library()

#Add member
member1 = Member(member_id=101, name="Pekka")
library.add_member(member1)

#Add books to library
book1 = Book(title="Book 1", author="Author 1", isbn="ISBN001")
book2 = Book(title="Book 2", author="Author 2", isbn="ISBN002")
library.add_item(book1)
library.add_item(book2)

#Member borrows books with due dates
due_date_book1 = datetime.now() + timedelta(days=7)  #Due in 7 days
member1.borrow_item(book1, due_date_book1)

due_date_book2 = datetime.now() + timedelta(days=14)  #Due in 14 days
member1.borrow_item(book2, due_date_book2)

#Time passing (10 days overdue)
today_date = datetime.now() + timedelta(days=10)

#Calculate fines for the member
total_fine = member1.calculate_fines(today_date)
print(f"Total Fine for {member1.name}: ${total_fine}")

#Member returns a book
member1.return_item(book1)

#Calculate fines again after returning the book
total_fine_after_return = member1.calculate_fines(today_date)
print(f"Total Fine for {member1.name} after returning book: ${total_fine_after_return}")

#Display available books in the library
library.display_available_books()
