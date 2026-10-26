
menu = {
    1: {"name": "Pizza", "price": 150},
    2: {"name": "Burger", "price": 80},
    3: {"name": "Pasta", "price": 120},
    4: {"name": "Sandwich", "price": 60},
    5: {"name": "Cold Drink", "price": 40}
}

order = []

while True:
    print("\n===== RESTAURANT ORDER SYSTEM =====")
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Order")
    print("4. Generate Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n---------- MENU ----------")

        for item_id, item in menu.items():
            print(
                item_id, ".",
                item["name"],
                "- Rs.", item["price"]
            )

    elif choice == "2":
        print("\nEnter food item number:")
        item_id = int(input("Item number: "))

        if item_id in menu:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                order.append({
                    "name": menu[item_id]["name"],
                    "price": menu[item_id]["price"],
                    "quantity": quantity
                })

                print("Item added to your order!")
            else:
                print("Quantity must be greater than zero.")

        else:
            print("Invalid item number!")

    elif choice == "3":
        print("\n---------- YOUR ORDER ----------")

        if len(order) == 0:
            print("Your order is empty.")

        else:
            for item in order:
                total = item["price"] * item["quantity"]

                print(
                    item["name"],
                    "x", item["quantity"],
                    "= Rs.", total
                )

    elif choice == "4":
        print("\n========== FINAL BILL ==========")

        if len(order) == 0:
            print("No items ordered.")

        else:
            grand_total = 0

            for item in order:
                total = item["price"] * item["quantity"]
                grand_total += total

                print(
                    item["name"],
                    "-", item["quantity"],
                    "x Rs.", item["price"],
                    "= Rs.", total
                )

            print("-------------------------------")
            print("Grand Total: Rs.", grand_total)
            print("Thank you for visiting!")

    elif choice == "5":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice! Please try again.")
