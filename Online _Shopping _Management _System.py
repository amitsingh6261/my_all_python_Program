
products = {
    1: {"name": "Laptop", "price": 45000, "stock": 5},
    2: {"name": "Mobile", "price": 15000, "stock": 10},
    3: {"name": "Headphones", "price": 1000, "stock": 15},
    4: {"name": "Keyboard", "price": 700, "stock": 8},
    5: {"name": "Mouse", "price": 400, "stock": 20}
}

cart = {}

while True:
    print("===== ONLINE SHOPPING SYSTEM =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("----- AVAILABLE PRODUCTS -----")

        for product_id, product in products.items():
            print(product_id, product["name"])
            print("Price: Rs.", product["price"])
            print("Stock:", product["stock"])

    elif choice == "2":
        product_id = int(input("Enter product ID: "))

        if product_id in products:
            quantity = int(input("Enter quantity: "))

            if quantity > 0 and quantity <= products[product_id]["stock"]:
                cart[product_id] = cart.get(product_id, 0) + quantity
                products[product_id]["stock"] -= quantity
                print("Product added to cart!")

            else:
                print("Invalid quantity or insufficient stock!")

        else:
            print("Product not found!")

    elif choice == "3":
        print("----- YOUR CART -----")

        if not cart:
            print("Your cart is empty.")

        else:
            for product_id, quantity in cart.items():
                product = products[product_id]
                total = product["price"] * quantity

                print(product["name"], "x", quantity, "= Rs.", total)

    elif choice == "4":
        product_id = int(input("Enter product ID to remove: "))

        if product_id in cart:
            products[product_id]["stock"] += cart[product_id]
            del cart[product_id]
            print("Product removed from cart!")

        else:
            print("Product not found in cart!")

    elif choice == "5":
        print("========== FINAL BILL ==========")

        if not cart:
            print("Your cart is empty.")

        else:
            grand_total = 0

            for product_id, quantity in cart.items():
                product = products[product_id]
                total = product["price"] * quantity
                grand_total += total

                print(product["name"], "x", quantity, "= Rs.", total)

            print("-------------------------------")
            print("Total Amount: Rs.", grand_total)
            print("Thank you for shopping!")

            cart.clear()

    elif choice == "6":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice!")
