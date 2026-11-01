
trains = {
    1: {"name": "Indore Express", "source": "Indore",
        "destination": "Bhopal", "seats": 5, "price": 200},

    2: {"name": "Delhi Express", "source": "Bhopal",
        "destination": "Delhi", "seats": 5, "price": 700},

    3: {"name": "Mumbai Express", "source": "Indore",
        "destination": "Mumbai", "seats": 5, "price": 900}
}

bookings = []
pnr_number = 1001

while True:
    print("===== RAILWAY RESERVATION SYSTEM =====")
    print("1. View Trains")
    print("2. Book Ticket")
    print("3. View All Bookings")
    print("4. Search PNR")
    print("5. Cancel Ticket")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("----- TRAIN DETAILS -----")

        for train_id, train in trains.items():
            print("\nTrain ID:", train_id)
            print("Train Name:", train["name"])
            print("From:", train["source"])
            print("To:", train["destination"])
            print("Available Seats:", train["seats"])
            print("Ticket Price: Rs.", train["price"])

    elif choice == "2":
        train_id = int(input("Enter Train ID: "))

        if train_id in trains:
            if trains[train_id]["seats"] > 0:
                name = input("Enter passenger name: ")
                age = int(input("Enter passenger age: "))

                booking = {
                    "pnr": pnr_number,
                    "name": name,
                    "age": age,
                    "train": trains[train_id]["name"],
                    "price": trains[train_id]["price"]
                }

                bookings.append(booking)
                trains[train_id]["seats"] -= 1

                print("Ticket booked successfully!")
                print("Your PNR Number:", pnr_number)

                pnr_number += 1

            else:
                print("No seats available!")

        else:
            print("Invalid Train ID!")

    elif choice == "3":
        print("----- ALL BOOKINGS -----")

        if not bookings:
            print("No bookings found.")

        else:
            for booking in bookings:
                print("PNR:", booking["pnr"])
                print("Passenger:", booking["name"])
                print("Train:", booking["train"])
                print("Price: Rs.", booking["price"])

    elif choice == "4":
        search_pnr = int(input("Enter PNR Number: "))
        found = False

        for booking in bookings:
            if booking["pnr"] == search_pnr:
                print("\nBooking Found!")
                print("Passenger:", booking["name"])
                print("Age:", booking["age"])
                print("Train:", booking["train"])
                print("Price: Rs.", booking["price"])
                found = True
                break

        if not found:
            print("PNR Number not found!")

    elif choice == "5":
        cancel_pnr = int(input("Enter PNR Number: "))
        found = False

        for booking in bookings:
            if booking["pnr"] == cancel_pnr:

                for train_id, train in trains.items():
                    if train["name"] == booking["train"]:
                        train["seats"] += 1
                        break

                bookings.remove(booking)
                print("Ticket cancelled successfully!")
                found = True
                break

        if not found:
            print("Booking not found!")

    elif choice == "6":
        print("Thank you for using Railway Reservation System!")
        break

    else:
        print("Invalid choice! Please try again.")
