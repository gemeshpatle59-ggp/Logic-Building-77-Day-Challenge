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


