from database import Database, Book, Member

class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.password = password
        self.loans = []

    def calculate_fines(self):
        today = datetime.now()
        fine_total = 0
        for loan in self.loans:
            if loan.due_date < today:
                overdue_days = (today - loan.due_date).days
                fine_total += 1 * overdue_days  # Assuming $1 fine per overdue day
        return fine_total

class Library:
    def __init__(self, db):
        self.db = db

    def add_book(self, title, author):
        self.db.add_book(Book(title, author))

    def add_member(self, member_id, name, password):
        self.db.add_member(Member(member_id, name, password))

    def borrow_book(self, title, member_id):
        return self.db.borrow_book(title, member_id)

    def return_book(self, title, member_id):
        return self.db.return_book(title, member_id)

    def search_books(self, query=""):
        return self.db.search_books(query)

    def validate_member(self, member_id, password):
        return self.db.validate_member(member_id, password)