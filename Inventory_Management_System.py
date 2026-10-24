
inventory = {}


def add_product():
    product_id = input("Enter product ID: ")

    if product_id in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: Rs. "))
        quantity = int(input("Enter product quantity: "))

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative!")
            return

        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid price and quantity!")


def view_inventory():
    if not inventory:
        print("Inventory is empty!")
        return

    print("===== INVENTORY =====")

    for product_id, product in inventory.items():
        print("Product ID:", product_id)
        print("Name:", product["name"])
        print("Price: Rs.", product["price"])
        print("Quantity:", product["quantity"])
        print("---------------------")


def search_product():
    product_id = input("Enter product ID to search: ")

    if product_id in inventory:
        product = inventory[product_id]

        print("Name:", product["name"])
        print("Price: Rs.", product["price"])
        print("Quantity:", product["quantity"])
    else:
        print("Product not found!")


def update_stock():
    product_id = input("Enter product ID: ")

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Quantity must be positive!")
            return

        inventory[product_id]["quantity"] += quantity
        print("Stock updated successfully!")

    except ValueError:
        print("Enter a valid quantity!")


def show_total_value():
    total = 0

    for product in inventory.values():
        total += product["price"] * product["quantity"]

    print("Total Inventory Value: Rs.", round(total, 2))


while True:
    print("===== INVENTORY MANAGEMENT =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Add Stock")
    print("5. Calculate Inventory Value")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        search_product()
    elif choice == "4":
        update_stock()
    elif choice == "5":
        show_total_value()
    elif choice == "6":
        print("Thank you for using Inventory Management!")
        break
    else:
        print("Invalid choice! Try again.")
