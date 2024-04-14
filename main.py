from interface import main
from library_system import Library
from database import Database

if __name__ == "__main__":
    db = Database()
    library = Library(db)
    main(library)
