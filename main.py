from db import get_available_rooms


def main():
    while True:
        print("\n==== DK HOTEL ====")
        print("1. View Rooms")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rooms = get_available_rooms()
            for room in rooms:
                print(
                    f"Room: {room[0]} | Type: {room[1]} | Capacity: {room[2]} | Price: {float(room[3])}")

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid user input")


main()
