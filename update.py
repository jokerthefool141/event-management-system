import helpers


def update_participant():
    '''
    Updates an existing participant's name and event
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No participants to update.")
        return

    import participants
    participants.view_participants()

    choice = input("\nEnter the participant number to update: ")
    helpers.new_line()
    helpers.print_separator()

    if not helpers.is_number(choice):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    current = lines[choice - 1].strip().split("|")

    print("\nCurrent Name : " + current[0].strip())
    print("\nCurrent Event: " + current[1].strip() + " | " +
          current[2].strip() + " | " + current[3].strip())

    helpers.new_line()
    helpers.print_separator()
    new_name = input("\nEnter new participant name: ").strip()
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

    if new_event_choice < 1 or new_event_choice > len(event_lines):

        print("\nInvalid selection.\n")
        helpers.print_separator()
        return

    new_event = event_lines[new_event_choice - 1].strip()

    lines[choice - 1] = new_name + "|" + new_event + "\n"

    file = open("participants.txt", "w")
    file.writelines(lines)
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

    if len(lines) == 0:
        print("No events to update.")
        return

    import events
    events.view_events()

    choice = input("Enter the event number to update: ")
    if not helpers.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    current = lines[choice - 1].strip().split("|")
    print("Current Event Name : " + current[0].strip())
    print("Current Date       : " + current[1].strip())
    print("Current Venue      : " + current[2].strip())

    new_name = input(
        "Enter new event name (or press Enter to keep current): ").strip()
    if not new_name:
        new_name = current[0].strip()

    new_date = input(
        "Enter new event date (or press Enter to keep current): ").strip()
    if not new_date:
        new_date = current[1].strip()

    new_venue = input(
        "Enter new event venue (or press Enter to keep current): ").strip()
    if not new_venue:
        new_venue = current[2].strip()

    lines[choice - 1] = new_name + "|" + new_date + "|" + new_venue + "\n"

    file = open("events.txt", "w")
    file.writelines(lines)
    file.close()

    old_event_name = current[0].strip()

    file = open("participants.txt", "r")
    participant_lines = file.readlines()
    file.close()

    updated_count = 0
    i = 0
    while i < len(participant_lines):
        parts = participant_lines[i].strip().split("|")

        if len(parts) >= 2 and parts[1].strip() == old_event_name:
            participant_lines[i] = parts[0].strip(
            ) + "|" + new_name + "|" + new_date + "|" + new_venue + "\n"
            updated_count += 1
        i += 1

    file = open("participants.txt", "w")
    file.writelines(participant_lines)
    file.close()

    print("Event updated successfully!")
    if updated_count > 0:
        print(str(updated_count) +
              " participant(s) linked to this event were also updated.")


# UPDATE ATTENDANCE

def update_attendance():
    '''
    Updates a participant's attendance status (Present / Absent)
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No attendance records to update.")
        return

    import attendance
    attendance.view_attendance()

    choice = input("Enter the attendance record number to update: ")
    if not helpers.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    current = lines[choice - 1].strip().split("|")
    print("Participant : " + current[0].strip())
    print("Event       : " + current[1].strip())
    print("Status      : " + current[2].strip())

    print("\nAttendance Status Options:")
    print("  1. Present")
    print("  2. Absent")

    status_choice = input("Enter new status (1 or 2): ")
    if not helpers.is_number(status_choice):
        print("Invalid selection.")
        return

    status_choice = int(status_choice)
    if status_choice == 1:
        new_status = "Present"
    elif status_choice == 2:
        new_status = "Absent"
    else:
        print("Invalid selection.")
        return

    lines[choice - 1] = current[0].strip() + "|" + current[1].strip() + \
        "|" + new_status + "\n"

    file = open("attendance.txt", "w")
    file.writelines(lines)
    file.close()

    print("Attendance updated successfully!")
    print(current[0].strip() + " is now marked as " + new_status + ".")
