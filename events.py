import helpers


def create_event():
    '''
    Creates and adds a new event

    '''

    helpers.print_title("===== EVENT MENU =====")

    event_name = input(
        "\nEnter the event name you want to add: ").strip().title()

    helpers.new_line()
    helpers.print_line()

    date = input("\nEnter event date: ").strip().title()

    helpers.new_line()
    helpers.print_line()

    venue = input("\nEnter event venue: ").strip().title()

    helpers.new_line()
    helpers.print_line()

    if not event_name or not date or not venue:

        print("\nFields cannot be empty. Please try again.\n")
        helpers.print_separator()

    else:

        file = open("events.txt", "r")
        lines = file.readlines()
        file.close()

        already_exists = False

        for line in lines:

            parts = helpers.split_record(line)

            if len(parts) >= 3:

                existing_event = parts[0].strip()
                existing_date = parts[1].strip()
                existing_venue = parts[2].strip()

                if (
                    existing_event == event_name and
                    existing_date == date and
                    existing_venue == venue
                ):
                    already_exists = True
                    break

        if already_exists:

            print("\nEvent already exists.\n")
            helpers.print_separator()
            return

        file = open("events.txt", "a")
        file.write(event_name + "|" + date + "|" + venue + "\n")
        file.close()

        print("\nEvent added successfully!\n")
        helpers.print_separator()


def view_events():
    '''
    Displays all events from events.txt
    '''

    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:

        helpers.print_separator()
        print("\nNo events found.\n")
        helpers.print_separator()
        return

    helpers.print_title("===== EVENT LIST =====")
    helpers.new_line()

    print(helpers.custom_ljust("No.", 5) +
          helpers.custom_ljust("Event Name", 25) +
          helpers.custom_ljust("Date", 25) +
          helpers.custom_ljust("Venue", 20))

    helpers.new_line()
    helpers.print_line()

    valid_rows = helpers.get_valid_event_rows(lines)

    if len(valid_rows) == 0:

        print("\nNo valid events found.\n")
        helpers.print_separator()
        return

    count = 1

    for parts in valid_rows:

        event_name = parts[0].strip()
        date = parts[1].strip()
        venue = parts[2].strip()

        helpers.new_line()

        print(
            helpers.custom_ljust(str(count), 5) +
            helpers.custom_ljust(event_name, 25) +
            helpers.custom_ljust(date, 25) +
            helpers.custom_ljust(venue, 20)
        )

        count += 1

    helpers.new_line()
    helpers.print_line()
    helpers.new_line()
    helpers.print_separator()


def delete_event():
    '''
    Removes an event from events.txt based on its number or name
    '''

    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()

    valid_rows = helpers.get_valid_event_rows(lines)
    valid_indexes = helpers.get_valid_event_indexes(lines)

    if len(valid_rows) == 0:

        helpers.print_separator()
        print("\nNo events found\n")
        helpers.print_separator()
        return

    view_events()

    choice = input("\nEnter the event number to remove: ").strip()
    helpers.new_line()

    if not helpers.is_number(choice):

        helpers.print_separator()
        print("\nInvalid input. Please enter a valid number.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(valid_rows):

        helpers.print_separator()
        print("\nPlease try again.\n")
        helpers.print_separator()
        return

    # Get Event Details

    real_index = valid_indexes[choice - 1]

    selected_event = lines[real_index].strip()
    event_parts = selected_event.split("|")

    if len(event_parts) < 3:

        helpers.print_separator()
        print("\nSelected event contains invalid/corrupted data.\n")
        helpers.print_separator()
        return

    event_name = event_parts[0].strip()
    date = event_parts[1].strip()
    venue = event_parts[2].strip()

    helpers.new_line()
    helpers.print_separator()

    print("\nWARNING!")
    print("You are about to permanently delete:")
    print("- The selected event.")
    print("- All participants registered for this event.")
    print("- All attendance records related to this event.\n")

    helpers.print_separator()

    while True:

        confirm = input(
            "\nAre you sure you want to delete this event? (yes/no): ").strip().lower()
        helpers.new_line()

        if confirm == "yes":
            break

        elif confirm == "no":

            helpers.print_separator()
            print("\nEvent deletion canceled.\n")
            helpers.print_separator()
            return

        else:
            helpers.print_separator()
            print("\nInvalid input. Please enter 'yes' or 'no' only.\n")
            helpers.print_separator()

    # Delete Event

    lines.pop(real_index)

    file = open("events.txt", "w")
    file.writelines(lines)
    file.close()

    # Delete Participants

    file = open("participants.txt", "r")
    participant_lines = file.readlines()
    file.close()

    updated_participants = []

    for line in participant_lines:

        parts = line.strip().split("|")

        if len(parts) >= 4:

            ppt_event_name = parts[1].strip()
            ppt_date = parts[2].strip()
            ppt_venue = parts[3].strip()

            if not (ppt_event_name == event_name and
                    ppt_date == date and
                    ppt_venue == venue):

                updated_participants.append(line)

        else:
            updated_participants.append(line)

    file = open("participants.txt", "w")
    file.writelines(updated_participants)
    file.close()

    # Delete Attendance

    file = open("attendance.txt", "r")
    attendance_lines = file.readlines()
    file.close()

    updated_attendance = []

    for line in attendance_lines:

        parts = line.strip().split("|")

        if len(parts) >= 5:

            atn_event_name = parts[1].strip()
            atn_date = parts[2].strip()
            atn_venue = parts[3].strip()

            if not (atn_event_name == event_name and
                    atn_date == date and
                    atn_venue == venue):

                updated_attendance.append(line)

        else:
            updated_attendance.append(line)

    file = open("attendance.txt", "w")
    file.writelines(updated_attendance)
    file.close()

    helpers.print_separator()
    print("\nEvent and all related records deleted successfully.\n")
    helpers.print_separator()


def events_menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("===== EVENT MENU =====")
        print("\n1.) Create Event\n")
        helpers.print_line()
        print("\n2.) View Events\n")
        helpers.print_line()
        print("\n3.) Update Event\n")
        helpers.print_line()
        print("\n4.) Delete Event\n")
        helpers.print_line()
        print("\n5.) Back to Main Menu\n")
        helpers.print_separator()

        choice = input("\nEnter your choice: ").strip()
        helpers.new_line()

        if choice == "1":
            create_event()
            helpers.pause()

        elif choice == "2":
            view_events()
            helpers.pause()

        elif choice == "3":
            import update
            update.update_event()
            helpers.pause()

        elif choice == "4":
            delete_event()
            helpers.pause()

        elif choice == "5":
            break

        else:
            helpers.print_separator()
            print("\nInvalid choice. Please try again.")
