import helpers


def update_participant():
    '''
    Updates an existing participant's name and event
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo participants found.\n")
        helpers.print_separator()
        return

    import participants
    participants.view_participants()

    valid_rows = helpers.get_valid_participant_rows(lines)
    valid_indexes = helpers.get_valid_participant_indexes(lines)

    choice = input("\nEnter the participant number to update: ")
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
    current = lines[real_index].strip().split("|")

    if len(current) < 4:

        print("\nSelected participant contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Participant : " + current[0].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Event      : " + current[1].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Date        : " + current[2].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Venue       : " + current[3].strip())
    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()

    new_name = input("\nEnter new participant name: ").strip().title()
    helpers.new_line()

    if not new_name:

        helpers.new_line()
        helpers.print_separator()
        print("\nInvalid input. Name cannot be empty.\n")
        helpers.print_separator()
        return

    file = open("events.txt", "r")
    event_lines = file.readlines()
    file.close()

    if len(event_lines) == 0:

        helpers.print_separator()
        print("\nNo events available to assign.\n")
        helpers.print_separator()
        return

    import events
    events.view_events()

    new_event_choice = input(
        "\nEnter the new event number for this participant: ")
    helpers.new_line()
    helpers.print_separator()

    if not helpers.is_number(new_event_choice):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    new_event_choice = int(new_event_choice)

    valid_event_indexes = helpers.get_valid_event_indexes(event_lines)
    valid_event_rows = helpers.get_valid_event_rows(event_lines)

    if new_event_choice < 1 or new_event_choice > len(valid_event_rows):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    event_real_index = valid_event_indexes[new_event_choice - 1]

    new_event = event_lines[event_real_index].strip()

    lines[real_index] = new_name + "|" + new_event + "\n"

    file = open("participants.txt", "w")
    file.writelines(lines)
    file.close()

    old_name = current[0].strip()
    old_event = current[1].strip()
    old_date = current[2].strip()
    old_venue = current[3].strip()

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    i = 0

    while i < len(attendance_lines):

        parts = attendance_lines[i].strip().split("|")

        if len(parts) >= 5:

            attendance_name = parts[0].strip()
            attendance_event = parts[1].strip()
            attendance_date = parts[2].strip()
            attendance_venue = parts[3].strip()
            attendance_status = parts[4].strip()

            if (
                attendance_name == old_name and
                attendance_event == old_event and
                attendance_date == old_date and
                attendance_venue == old_venue
            ):

                attendance_lines[i] = (
                    new_name + "|" +
                    old_event + "|" +
                    old_date + "|" +
                    old_venue + "|" +
                    attendance_status + "\n"
                )
        i += 1

    file = open("attendance.txt", "w")
    file.writelines(attendance_lines)
    file.close()

    print("\nParticipant updated successfully!\n")
    helpers.print_separator()


# UPDATE EVENT

def update_event():
    '''
    Updates an existing event's name, date, and venue
    '''

    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()

    valid_rows = helpers.get_valid_event_rows(lines)
    valid_indexes = helpers.get_valid_event_indexes(lines)

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo events found.\n")
        helpers.print_separator()
        return

    import events
    events.view_events()

    choice = input("\nEnter the event number to update: ")
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
    current = lines[real_index].strip().split("|")

    if len(current) < 3:

        helpers.print_separator()
        print("\nSelected event contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Event Name : " + current[0].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Date       : " + current[1].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Venue      : " + current[2].strip())
    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()

    new_name = input(
        "\nEnter new event name (or press Enter to keep current): ").strip().title()
    helpers.new_line()
    helpers.print_line()

    if not new_name:
        new_name = current[0].strip()

    new_date = input(
        "\nEnter new event date (or press Enter to keep current): ").strip().title()
    helpers.new_line()
    helpers.print_line()

    if not new_date:
        new_date = current[1].strip()

    new_venue = input(
        "\nEnter new event venue (or press Enter to keep current): ").strip().title()
    helpers.new_line()

    if not new_venue:
        new_venue = current[2].strip()

    lines[real_index] = new_name + "|" + new_date + "|" + new_venue + "\n"

    file = open("events.txt", "w")
    file.writelines(lines)
    file.close()

    file = open("participants.txt", "r")
    participant_lines = file.readlines()
    file.close()

    updated_count = 0

    i = 0

    while i < len(participant_lines):

        parts = participant_lines[i].strip().split("|")

        if (len(parts) >= 4 and
            parts[1].strip() == current[0].strip() and
            parts[2].strip() == current[1].strip() and
                parts[3].strip() == current[2].strip()):

            participant_lines[i] = parts[0].strip(
            ) + "|" + new_name + "|" + new_date + "|" + new_venue + "\n"

            updated_count += 1

        i += 1

    file = open("participants.txt", "w")
    file.writelines(participant_lines)
    file.close()

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    i = 0

    while i < len(attendance_lines):

        parts = attendance_lines[i].strip().split("|")

        if len(parts) >= 5:

            old_event_name = parts[1].strip()
            old_date = parts[2].strip()
            old_venue = parts[3].strip()

            if (old_event_name == current[0].strip() and
                old_date == current[1].strip() and
                    old_venue == current[2].strip()):

                attendance_lines[i] = (
                    parts[0].strip() + "|" +
                    new_name + "|" +
                    new_date + "|" +
                    new_venue + "|" +
                    parts[4].strip() + "\n"
                )

        i += 1

    file = open("attendance.txt", "w")
    file.writelines(attendance_lines)
    file.close()

    helpers.print_separator()
    print("\nEvent updated successfully!\n")
    helpers.print_separator()

    if updated_count > 0:

        helpers.new_line()
        print(str(updated_count) +
              " participant(s) linked to this event were also updated.\n")
        helpers.print_separator()


# UPDATE ATTENDANCE

def update_attendance():
    '''
    Updates a participant's attendance status (Present / Absent)
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

    import attendance
    attendance.view_attendance()

    choice = input("\nEnter the attendance record number to update: ")
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
    current = lines[real_index].strip().split("|")

    if len(current) < 5:

        helpers.print_separator()
        print("\nSelected attendance record contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    helpers.print_separator()
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Participant : " + current[0].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Event         : " + current[1].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Date          : " + current[2].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Venue         : " + current[3].strip())
    helpers.new_line()
    helpers.print_line()
    print("\nCurrent Status        : " + current[4].strip())
    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()

    print("\nAttendance Status Options:\n")
    helpers.print_line()
    print("\n  1. Present\n")
    helpers.print_line()
    print("\n  2. Absent\n")
    helpers.print_separator()

    status_choice = input("\nEnter new status (1 or 2): ")
    helpers.new_line()

    if not helpers.is_number(status_choice):

        helpers.print_separator()
        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    status_choice = int(status_choice)

    if status_choice == 1:
        new_status = "Present"

    elif status_choice == 2:
        new_status = "Absent"

    else:
        helpers.print_separator()
        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    participant_name = current[0].strip()
    event_name = current[1].strip()
    date = current[2].strip()
    venue = current[3].strip()

    lines[real_index] = (
        participant_name + "|" +
        event_name + "|" +
        date + "|" +
        venue + "|" +
        new_status + "\n"
    )

    file = open("attendance.txt", "w")
    file.writelines(lines)
    file.close()

    helpers.print_separator()
    print("\nAttendance updated successfully!\n")
    helpers.print_separator()
    helpers.new_line()
    print(current[0].strip() + " is now marked as " + new_status + ".\n")
    helpers.print_separator()
