import events
import participants
import update
import attendance


def menu():
    while True:
        print("\n" * 2)
        print("=" * 55)
        print("           ==== EVENT MANAGEMENT SYSTEM ====")
        print("=" * 55)
        print()
        print("-" * 55)
        print("1.) Add Event")
        print("-" * 55)
        print("2.) View Events")
        print("-" * 55)
        print("3.) Register Participant")
        print("-" * 55)
        print("4.) View Participants")
        print("-" * 55)
        print("5.) Update Participant")
        print("-" * 55)
        print("6.) Delete Participant")
        print("-" * 55)
        print("7.) Mark Attendance")
        print("-" * 55)
        print("8.) View Attendance")
        print("-" * 55)
        print("9.) Exit")
        print("-" * 55)
        print()
        print("=" * 55)
        print()

        choice = input("Enter your choice: ")
        print()
        print("=" * 55)
        print()

        if choice == "1":
            events.create_event()
            input("\nPress Enter to continue...")

        elif choice == "2":
            events.view_events()
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    menu()
