# Importing project modules

import events
import participants
import update
import attendance
import helpers


# Main menu function for the Event Management System

def menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("==== EVENT MANAGEMENT SYSTEM ====")

        print("\n1.) Add Event\n")
        helpers.print_line()

        print("\n2.) View Events\n")
        helpers.print_line()

        print("\n3.) Register Participant\n")
        helpers.print_line()

        print("\n4.) View Participants\n")
        helpers.print_line()

        print("\n5.) Update Participant\n")
        helpers.print_line()

        print("\n6.) Delete Participant\n")
        helpers.print_line()

        print("\n7.) Mark Attendance\n")
        helpers.print_line()

        print("\n8.) View Attendance\n")
        helpers.print_line()

        print("\n9.) Clear Screen\n")
        helpers.print_line()

        print("\n10.) Exit\n")

        helpers.print_separator()

        choice = input("\nEnter your choice: ")

        helpers.new_line()

        if choice == "1":
            events.create_event()
            helpers.pause()

        elif choice == "2":
            events.view_events()
            helpers.pause()

        elif choice == "3":
            participants.register_participant()
            helpers.pause()

        elif choice == "4":
            participants.view_participants()
            helpers.pause()

        elif choice == "5":
            update.update_participant()
            helpers.pause()

        elif choice == "6":
            attendance.delete_participant()
            helpers.pause()

        elif choice == "7":
            attendance.mark_attendance()
            helpers.pause()

        elif choice == "8":
            attendance.view_attendance()
            helpers.pause()

        elif choice == "9":
            helpers.clear_screen()

        elif choice == "10":
            break

        else:
            helpers.print_separator()
            helpers.new_line()
            print("Invalid choice. Please try again.")

    helpers.print_separator()
    print("\nExiting the Event Management System. Goodbye!\n")
    helpers.print_separator()
    helpers.new_line()


if __name__ == "__main__":
    menu()
