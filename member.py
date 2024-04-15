class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name 
        self.password = password 
        self.loans = []  #List of books currently borrowed by the member