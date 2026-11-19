# Create a simple library management program with add/search/issue/return operations.

library = {}

# 1. Add Book
def add_book():

    book_id = int(input("Enter Book ID: "))

    if book_id in library:
        print("Book already exists!")

    else:
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0!")
            return

        library[book_id] = {
            "name": name,
            "author": author,
            "quantity": quantity,
            "issued": 0
        }

        print("Book added successfully!")


# 2. Search Book
def search_book():

    book_id = int(input("Enter Book ID: "))

    if book_id in library:

        print("\nBook Found!")
        print("Book ID:", book_id)
        print("Name:", library[book_id]["name"])
        print("Author:", library[book_id]["author"])
        print("Available:", library[book_id]["quantity"])
        print("Issued:", library[book_id]["issued"])

    else:
        print("Book not found!")


# 3. Issue Book
def issue_book():

    book_id = int(input("Enter Book ID: "))

    if book_id in library:

        if library[book_id]["quantity"] > 0:

            library[book_id]["quantity"] -= 1
            library[book_id]["issued"] += 1

            print("Book issued successfully!")

        else:
            print("Book is currently unavailable!")

    else:
        print("Book not found!")

#  4. Return Book
def return_book():

    book_id = int(input("Enter Book ID: "))

    if book_id in library:

        if library[book_id]["issued"] > 0:

            library[book_id]["issued"] -= 1
            library[book_id]["quantity"] += 1

            print("Book returned successfully!")

        else:
            print("No issued copy of this book to return!")

    else:
        print("Book not found!")


# 5. Display All Books
def display_books():

    if len(library) == 0:
        print("Library is empty!")

    else:

        print("\n========== ALL BOOKS ==========")

        for book_id, details in library.items():

            print("\nBook ID:", book_id)
            print("Name:", details["name"])
            print("Author:", details["author"])
            print("Available:", details["quantity"])
            print("Issued:", details["issued"])

            print("-----------------------------")

