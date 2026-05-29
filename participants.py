import helpers


def register_participant():
    '''
    Registers a participant to an existing event
    '''

    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo events available.\n")
        helpers.print_separator()
        return

    import events
    events.view_events()

    valid_rows = helpers.get_valid_event_rows(lines)
    valid_indexes = helpers.get_valid_event_indexes(lines)

    choice = input("\nEnter the event number to register for: ")
    helpers.new_line()

    if not helpers.is_number(choice):

        helpers.print_separator()
        print("\nInvalid event selection.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(valid_rows):

        helpers.print_separator()
        print("\nInvalid event selection.\n")
        helpers.print_separator()
        return

    helpers.print_separator()
    participant_name = input("\nEnter participant name: ").strip().title()
    helpers.new_line()
    helpers.print_separator()

    if not participant_name:

        print("\nInvalid name.\n")
        helpers.print_separator()
        return

    real_index = valid_indexes[choice - 1]

    selected_event = lines[real_index].strip()
    selected_parts = selected_event.split("|")

    if len(selected_parts) < 3:

        print("\nSelected event contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    file = open("participants.txt", "a")
    file.write(participant_name + "|" + selected_event + "\n")
    file.close()

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    helpers.bubble_sort(lines)

    file = open("participants.txt", "w")
    file.writelines(lines)
    file.close()

    print("\nParticipant registered successfully!\n")
    helpers.print_separator()


def view_participants():
    '''
    Displays all participants from participants.txt
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo participants found.\n")
        helpers.print_separator()
        return

    helpers.print_title("===== PARTICIPANT LIST =====")
    helpers.new_line()

    print(
        helpers.custom_ljust("No.", 5) +
        helpers.custom_ljust("Participant Name", 25) +
        helpers.custom_ljust("Event Name", 25) +
        helpers.custom_ljust("Date", 20) +
        helpers.custom_ljust("Venue", 20)
    )

    helpers.new_line()
    helpers.print_line()

    valid_rows = helpers.get_valid_participant_rows(lines)

    if len(valid_rows) == 0:

        print("\nNo valid participants found.\n")
        helpers.print_separator()
        return

    count = 1

    for parts in valid_rows:

        participant_name = parts[0].strip()
        event_name = parts[1].strip()
        date = parts[2].strip()
        venue = parts[3].strip()

        helpers.new_line()

        print(
            helpers.custom_ljust(str(count), 5) +
            helpers.custom_ljust(participant_name, 25) +
            helpers.custom_ljust(event_name, 25) +
            helpers.custom_ljust(date, 20) +
            helpers.custom_ljust(venue, 20)
        )

        count += 1

    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()


def delete_participant():
    '''
    Deletes an existing participant
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    valid_rows = helpers.get_valid_participant_rows(lines)
    valid_indexes = helpers.get_valid_participant_indexes(lines)

    if len(valid_rows) == 0:

        helpers.print_separator()
        print("\nNo valid participants found.\n")
        helpers.print_separator()
        return

    view_participants()

    choice = input("\nEnter the participant number to delete: ")
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

    selected_participant = lines[real_index].strip()
    participant_parts = selected_participant.split("|")

    if len(participant_parts) < 4:

        print("\nSelected participant contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    participant_name = participant_parts[0].strip()
    participant_event = participant_parts[1].strip()
    participant_date = participant_parts[2].strip()
    participant_venue = participant_parts[3].strip()

    helpers.new_line()
    helpers.print_separator()

    print("\nWARNING!")
    print("You are about to permanently delete:")
    print("- The selected participant.")
    print("- All attendance records related to this participant.\n")

    helpers.print_separator()

    while True:

        confirm = input(
            "\nAre you sure you want to delete this participant? (yes/no): ").strip().lower()

        helpers.new_line()

        if confirm == "yes":
            break

        elif confirm == "no":

            helpers.print_separator()
            print("\nParticipant deletion canceled.\n")
            helpers.print_separator()
            return

        else:

            helpers.print_separator()
            print("\nInvalid input. Please enter 'yes' or 'no' only.\n")
            helpers.print_separator()

    lines.pop(real_index)

    file = open("participants.txt", "w")
    file.writelines(lines)
    file.close()

    # Delete Attendance

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    updated_attendance = []

    for line in attendance_lines:

        parts = helpers.split_record(line)

        if len(parts) >= 5:

            atn_event_name = parts[1].strip()
            atn_date = parts[2].strip()
            atn_venue = parts[3].strip()

            atn_participant_name = parts[0].strip()

            if not (atn_participant_name == participant_name and
                    atn_event_name == participant_event and
                    atn_date == participant_date and
                    atn_venue == participant_venue):

                updated_attendance.append(line)

        else:
            updated_attendance.append(line)

    file = open("attendance.txt", "w")
    file.writelines(updated_attendance)
    file.close()

    print("\nParticipant deleted successfully!\n")
    helpers.print_separator()


def participant_menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("===== PARTICIPANT MENU =====")
        helpers.new_line()
        print("\n1.) Register Participant\n")
        helpers.print_line()
        print("\n2.) View Participants\n")
        helpers.print_line()
        print("\n3.) Update Participant\n")
        helpers.print_line()
        print("\n4.) Delete Participant\n")
        helpers.print_line()
        print("\n5.) Back to Main Menu\n")
        helpers.print_separator()

        choice = input("\nEnter your choice: ").strip()
        helpers.new_line()

        if choice == "1":
            register_participant()
            helpers.pause()

        elif choice == "2":
            view_participants()
            helpers.pause()

        elif choice == "3":
            import update
            update.update_participant()
            helpers.pause()

        elif choice == "4":
            delete_participant()
            helpers.pause()

        elif choice == "5":
            break

        else:
            helpers.print_separator()
            print("\nInvalid choice. Please try again.")
