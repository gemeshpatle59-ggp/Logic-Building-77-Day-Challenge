"""
Create a contact-like dictionary program that can add, search, update, delete, and count entries.

"""

contacts = {}

while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Count Contacts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Contact
    if choice == 1:

        name = input("Enter name: ")
        number = input("Enter phone number: ")

        if name in contacts:
            print("Contact already exists!")
        else:
            contacts[name] = number
            print("Contact added successfully!")

    # 2. Search Contact
    elif choice == 2:

        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    # 3. Update Contact
    elif choice == 3:

        name = input("Enter name to update: ")

        if name in contacts:
            number = input("Enter new phone number: ")
            contacts[name] = number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # 4. Delete Contact
    elif choice == 4:

        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # 5. Display All Contacts
    elif choice == 5:

        if len(contacts) == 0:
            print("No contacts available!")
        else:
            print("\nAll Contacts:")

            for name, number in contacts.items():
                print(name, ":", number)

    # 6. Count Contacts
    elif choice == 6:

        print("Total Contacts:", len(contacts))

    # 7. Exit
    elif choice == 7:

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")