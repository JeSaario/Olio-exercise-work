from interface import main

if __name__ == "__main__":
    from library import Library
    from database import Database

    db = Database()
    library = Library(db)
    main(library)
