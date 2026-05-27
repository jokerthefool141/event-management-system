# Importing project modules

import events
import participants
import attendance
import helpers


# Main menu function for the Event Management System

def menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("==== EVENT MANAGEMENT SYSTEM ====")
        print("\n1.) Event Menu\n")
        helpers.print_line()
        print("\n2.) Participant Menu\n")
        helpers.print_line()
        print("\n3.) Attendance Menu\n")
        helpers.print_line()
        print("\n4.) Clear Screen\n")
        helpers.print_line()
        print("\n5.) Exit\n")
        helpers.print_separator()

        choice = input("\nEnter your choice: ")
        helpers.new_line()

        if choice == "1":
            events.events_menu()

        elif choice == "2":
            participants.participant_menu()

        elif choice == "3":
            attendance.attendance_menu()

        elif choice == "4":
            helpers.clear_screen()

        elif choice == "5":
            break

        else:
            helpers.print_separator()
            print("\nInvalid choice. Please try again.")

    helpers.new_line()
    helpers.print_separator()
    print("\nExiting the Event Management System. Goodbye!\n")
    helpers.print_separator()
    helpers.new_line()


if __name__ == "__main__":
    menu()
