import helpers


def mark_attendance():
    '''
    Records attendance of a participant
    '''

    file = open("participants.txt", "r")
    participant_lines = file.readlines()
    file.close()

    if len(participant_lines) == 0:

        helpers.print_separator()
        print("\nNo participants available.\n")
        helpers.print_separator()
        return

    import participants
    participants.view_participants()

    valid_rows = helpers.get_valid_participant_rows(participant_lines)
    valid_indexes = helpers.get_valid_participant_indexes(participant_lines)

    choice = input("\nEnter the participant number: ")
    helpers.new_line()
    helpers.print_separator()

    if not helpers.is_number(choice):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(valid_rows):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    real_index = valid_indexes[choice - 1]

    participant = participant_lines[real_index].strip()

    participant_parts = participant.split("|")

    if len(participant_parts) < 4:

        print("\nSelected participant contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    status = input("\nEnter attendance (Present/Absent): ").strip().title()
    helpers.new_line()
    helpers.print_separator()

    if status != "Present" and status != "Absent":

        print("\nInvalid attendance status.\n")
        helpers.print_separator()
        return

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    already_exists = False

    participant_name = participant_parts[0].strip()
    participant_event = participant_parts[1].strip()
    participant_date = participant_parts[2].strip()
    participant_venue = participant_parts[3].strip()

    for line in attendance_lines:

        parts = helpers.split_record(line)

        if len(parts) >= 5:

            attendance_name = parts[0].strip()
            attendance_event = parts[1].strip()
            attendance_date = parts[2].strip()
            attendance_venue = parts[3].strip()

            if (
                attendance_name == participant_name and
                attendance_event == participant_event and
                attendance_date == participant_date and
                attendance_venue == participant_venue
            ):

                already_exists = True
                break

    if already_exists:

        print("\nAttendance already recorded for this participant.\n")
        helpers.print_separator()
        return

    file = open("attendance.txt", "a")
    file.write(participant + "|" + status + "\n")
    file.close()

    print("\nAttendance recorded successfully!\n")
    helpers.print_separator()


def view_attendance():
    '''
    Displays all attendance records
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo attendance records found.\n")
        helpers.print_separator()
        return

    helpers.print_title("===== ATTENDANCE RECORDS =====")
    helpers.new_line()

    print(
        helpers.custom_ljust("No.", 5) +
        helpers.custom_ljust("Participant Name", 25) +
        helpers.custom_ljust("Event Name", 25) +
        helpers.custom_ljust("Date", 20) +
        helpers.custom_ljust("Venue", 20) +
        helpers.custom_ljust("Status", 15)
    )

    helpers.new_line()
    helpers.print_line()

    valid_rows = helpers.get_valid_attendance_rows(lines)

    if len(valid_rows) == 0:

        helpers.print_separator()
        print("\nNo valid attendance records found.\n")
        helpers.print_separator()
        return

    count = 1

    for record in valid_rows:

        helpers.new_line()

        print(
            helpers.custom_ljust(str(count), 5) +
            helpers.custom_ljust(record[0], 25) +
            helpers.custom_ljust(record[1], 25) +
            helpers.custom_ljust(record[2], 20) +
            helpers.custom_ljust(record[3], 20) +
            helpers.custom_ljust(record[4], 15)
        )

        count += 1

    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()


def delete_attendance():
    '''
    Deletes an attendance record
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

    valid_rows = helpers.get_valid_attendance_rows(lines)
    valid_indexes = helpers.get_valid_attendance_indexes(lines)

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo attendance records found.\n")
        helpers.print_separator()
        return

    if len(valid_rows) == 0:

        helpers.print_separator()
        print("\nNo valid attendance records found.\n")
        helpers.print_separator()
        return

    view_attendance()

    choice = input("\nEnter the attendance record number to delete: ")
    helpers.new_line()

    if not helpers.is_number(choice):

        helpers.print_separator()
        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(valid_rows):

        helpers.print_separator()
        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    real_index = valid_indexes[choice - 1]

    record_parts = lines[real_index].strip().split("|")

    if len(record_parts) >= 5:

        participant_name = record_parts[0].strip()
        event_name = record_parts[1].strip()
        date = record_parts[2].strip()
        venue = record_parts[3].strip()

        lines[real_index] = (
            participant_name + "|" +
            event_name + "|" +
            date + "|" +
            venue + "|" + "\n"
        )

    file = open("attendance.txt", "w")
    file.writelines(lines)
    file.close()

    helpers.print_separator()
    print("\nAttendance record deleted successfully!\n")
    helpers.print_separator()


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
