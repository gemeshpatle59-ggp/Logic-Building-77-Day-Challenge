# Create a simple inventory analyzer that tracks item quantities, searches items, updates stock, and identifies
# low-stock items.



inventory = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 8,
    "Monitor": 2,
    "Headphones": 6
}

# Display all items
def display_inventory():
    print("\n--- Inventory List ---")
    for item, quantity in inventory.items():
        print(item, ":", quantity)


# Search for an item
def search_item():
    item = input("Enter item name: ")

    if item in inventory:
        print(item, "Stock:", inventory[item])
    else:
        print("Item not found!")


# Update stock
def update_stock():
    item = input("Enter item name: ")

    if item in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[item] = quantity
        print("Stock updated successfully!")
    else:
        print("Item not found!")


# Find low-stock items
def low_stock():
    print("\n--- Low Stock Items ---")

    found = False

    for item, quantity in inventory.items():
        if quantity < 5:
            print(item, ":", quantity)
            found = True

    if not found:
        print("No low-stock items!")


# Main program
while True:
    print("\n===== INVENTORY ANALYZER =====")
    print("1. Display Inventory")
    print("2. Search Item")
    print("3. Update Stock")
    print("4. Low Stock Items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory()

    elif choice == "2":
        search_item()

    elif choice == "3":
        update_stock()

    elif choice == "4":
        low_stock()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")