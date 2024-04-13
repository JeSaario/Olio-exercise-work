class LibraryItem:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.reserved = False
        self.due_date = None

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            return True
        else:
            return False  #Item is already reserved

    def return_item(self):
        if self.reserved:
            self.reserved = False
            self.due_date = None  #Clear due date upon return
            return True
        else:
            return False  #Item is not reserved


class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item, due_date):
        if item.reserve():
            item.due_date = due_date
            self.borrowed_items.append(item)
            print(f"{self.name} borrowed '{item.title}'.")
            return True
        else:
            print(f"{item.title} is not available for borrowing.")
            return False

    def return_item(self, item):
        if item in self.borrowed_items:
            if item.return_item():
                self.borrowed_items.remove(item)
                print(f"{self.name} returned '{item.title}'.")
                return True
            else:
                print(f"Error returning '{item.title}'.")
                return False
        else:
            print(f"{self.name} did not borrow '{item.title}'.")

    def calculate_fines(self, today_date):
        total_fine = 0
        for item in self.borrowed_items:
            if item.due_date and item.due_date < today_date:
                days_overdue = (today_date - item.due_date).days
                fine_per_day = 1  #Example: 1€/day fine when overdue
                total_fine += days_overdue * fine_per_day
        return total_fine


class Library:
    def __init__(self):
        self.items = []
        self.members = {}

    def add_item(self, item):
        self.items.append(item)

    def add_member(self, member):
        self.members[member.member_id] = member


