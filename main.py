from db import get_available_rooms, room_booking, get_bookings, cancel_booking


def main():
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

            result = room_booking(name, room_id, check_in, check_out)
            print(result)

        elif choice == "3":
            bookings = get_bookings()

            for booking in bookings:
                print(
                    f"Booking ID: {booking[0]} | Name: {booking[1]} | Room ID: {booking[2]} | Check in: {booking[3]}, | Check out: {booking[4]}")

        elif choice == "4":
            try:
                booking_id = int(input("Enter your booking ID to cancel: "))
            except ValueError:
                print("Invalid booking ID")
                continue

            result = cancel_booking(booking_id)
            print(result)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid user input")


main()
