from db import get_available_rooms, room_booking, get_bookings, cancel_booking, login, register


def main():

    user_id = None

    while user_id is None:
        print("\n==== Welcome ====")
        print("1. Login")
        print("2. Register")

        choice = input("Choose option: ")
        if choice == "1":
            user_name = input("Enter username: ")
            user_password = input("Enter password: ")

            user_id = login(user_name, user_password)

            if user_id is None:
                print("Invalid credentials")

        elif choice == "2":
            user_name = input("Create username: ")
            user_password = input("Create password: ")

            result = register(user_name, user_password)
            print(result)

        else:
            print("Invalid choice")

    while True:
        print("\n==== DK HOTEL ====")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rooms = get_available_rooms()
            for room in rooms:
                print(
                    f"Room: {room[0]} | Type: {room[1]} | Capacity: {room[2]} | Price: {room[3]:.2f}")

        elif choice == "2":
            name = input("Enter your name: ")
            try:
                room_id = int(input("Enter room ID: "))
            except ValueError:
                print("Invalid room ID")
                continue

            check_in = input("Enter check in date (YYYY-MM-DD): ")
            check_out = input("Enter check out date (YYYY-MM-DD): ")

            if check_in >= check_out:
                print("\nInvalid date range (check-out must be after check-in)")
                continue

            result = room_booking(user_id, name, room_id, check_in, check_out)
            print(result)

        elif choice == "3":
            print("\n==== Your Bookings ====")
            bookings = get_bookings(user_id)

            if not bookings:
                print("No bookings found.")
            else:
                for booking in bookings:
                    print(
                        f"Booking ID: {booking[0]} | Name: {booking[1]} | Room ID: {booking[2]} | Check in: {booking[3]} | Check out: {booking[4]}")

        elif choice == "4":
            try:
                booking_id = int(input("Enter your booking ID to cancel: "))
            except ValueError:
                print("Invalid booking ID")
                continue

            confirm = input("Are you sure want to cancel? (yes/no): ").lower()

            if confirm != "yes":
                print("Cancellation aborted.")
                continue

            result = cancel_booking(user_id, booking_id)
            print(result)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid user input")


main()
