
movies = {
    "1": {"name": "Avengers", "price": 200, "seats": 50},
    "2": {"name": "Spider-Man", "price": 180, "seats": 40},
    "3": {"name": "Batman", "price": 150, "seats": 30}
}

bookings = []


def show_movies():
    print("\n===== AVAILABLE MOVIES =====")

    for movie_id, movie in movies.items():
        print(f"{movie_id}. {movie['name']}")
        print("Ticket Price: Rs.", movie["price"])
        print("Available Seats:", movie["seats"])
        print("------------------------")


def book_ticket():
    show_movies()

    movie_id = input("Enter movie number: ")

    if movie_id not in movies:
        print("Movie not found!")
        return

    try:
        seats = int(input("Enter number of tickets: "))

        if seats <= 0:
            print("Enter at least one ticket!")
            return

        movie = movies[movie_id]

        if seats > movie["seats"]:
            print("Sorry, not enough seats available!")
            return

        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty!")
            return

        total = seats * movie["price"]
        movie["seats"] -= seats

        bookings.append({
            "name": name,
            "movie": movie["name"],
            "seats": seats,
            "total": total
        })

        print("\n===== BOOKING CONFIRMED =====")
        print("Customer:", name)
        print("Movie:", movie["name"])
        print("Tickets:", seats)
        print("Total Amount: Rs.", total)

    except ValueError:
        print("Please enter a valid number!")


def view_bookings():
    if not bookings:
        print("No bookings available!")
        return

    print("\n===== ALL BOOKINGS =====")

    for i, booking in enumerate(bookings, start=1):
        print("Booking:", i)
        print("Customer:", booking["name"])
        print("Movie:", booking["movie"])
        print("Tickets:", booking["seats"])
        print("Amount: Rs.", booking["total"])
        print("------------------------")


while True:
    print("\n===== MOVIE TICKET BOOKING =====")
    print("1. Show Movies")
    print("2. Book Tickets")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_bookings()
    elif choice == "4":
        print("Thank you for using our booking system!")
        break
    else:
        print("Invalid choice! Try again.")
