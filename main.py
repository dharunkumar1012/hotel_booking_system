from db import get_available_rooms, room_booking


def main():
    while True:
        print("\n==== DK HOTEL ====")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rooms = get_available_rooms()
            for room in rooms:
                print(
                    f"Room: {room[0]} | Type: {room[1]} | Capacity: {room[2]} | Price: {room[3]:.2f}")

        elif choice == "2":
            name = input("Enter your name: ")
            room_id = int(input("Enter room ID: "))
            check_in = input("Enter check in date (YYYY-MM-DD): ")
            check_out = input("Enter check out date (YYYY-MM-DD): ")

            if check_in >= check_out:
                print("\nInvalid date range (check-out must be after check-in)")
                continue

            result = room_booking(name, room_id, check_in, check_out)
            print(result)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid user input")


main()
