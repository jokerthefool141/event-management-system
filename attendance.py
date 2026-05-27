import helpers


def mark_attendance():
    '''
    Records attendance of a participant
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No participants available.")
        return

    import participants
    participants.view_participants()

    choice = input("Enter the participant number: ")
    if not helpers.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    participant = lines[choice - 1].strip()

    status = input("Enter attendance (Present/Absent): ").strip()

    if status.lower() != "present" and status.lower() != "absent":
        print("Invalid attendance status.")
        return

    file = open("attendance.txt", "a")
    file.write(participant + "|" + status.title() + "\n")
    file.close()
    print("Attendance recorded successfully!")


def view_attendance():
    '''
    Displays all attendance records
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No attendance records found.")
        return

    print("\n===== ATTENDANCE RECORDS =====")

    count = 1

    for line in lines:
        record = line.strip().split("|")

        print(
            str(count) + ". " +
            record[0] + " | " +
            record[1] + " | " +
            record[2] + " | " +
            record[3] + " | " +
            record[4]
        )

        count += 1


def delete_attendance():
    '''
    Deletes an attendance record
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No attendance records found.")
        return

    view_attendance()

    choice = input("Enter the attendance record number to delete: ")

    if not helpers.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    lines.pop(choice - 1)

    file = open("attendance.txt", "w")
    file.writelines(lines)
    file.close()

    print("Attendance record deleted successfully!")


def attendance_menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("==== ATTENDANCE MENU ====")
        print("\n1.) Mark Attendance\n")
        helpers.print_line()
        print("\n2.) View Attendance\n")
        helpers.print_line()
        print("\n3.) Update Attendance\n")
        helpers.print_line()
        print("\n4.) Delete Attendance\n")
        helpers.print_line()
        print("\n5.) Back to Main Menu\n")
        helpers.print_separator()

        choice = input("\nEnter your choice: ").strip()
        helpers.new_line()

        if choice == "1":
            mark_attendance()
            helpers.pause()

        elif choice == "2":
            view_attendance()
            helpers.pause()

        elif choice == "3":
            import update
            update.update_attendance()
            helpers.pause()

        elif choice == "4":
            delete_attendance()
            helpers.pause()

        elif choice == "5":
            break

        else:
            helpers.print_separator()
            print("\nInvalid choice. Please try again.")
