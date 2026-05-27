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

    choice = input("\nEnter the event number to register for: ")
    helpers.new_line()

    if not helpers.is_number(choice):

        helpers.print_separator()
        print("\nInvalid event selection.\n")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):

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

    selected_event = lines[choice - 1].strip()

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

    helpers.print_title("==== PARTICIPANT LIST ====")
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

    for i in range(len(lines)):
        line = lines[i].strip()
        parts = line.split("|")

        if len(parts) >= 4:
            participant_name = parts[0].strip()
            event_name = parts[1].strip()
            date = parts[2].strip()
            venue = parts[3].strip()

            helpers.new_line()
            print(
                helpers.custom_ljust(str(i + 1), 5) +
                helpers.custom_ljust(participant_name, 25) +
                helpers.custom_ljust(event_name, 25) +
                helpers.custom_ljust(date, 20) +
                helpers.custom_ljust(venue, 20))

        else:
            print("\nSkipped invalid data.\n")

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

    if len(lines) == 0:
        print("No participants to delete.")
        return

    view_participants()

    choice = input("Enter the participant number to delete: ")

    if not helpers.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    lines.pop(choice - 1)

    file = open("participants.txt", "w")
    file.writelines(lines)
    file.close()

    print("Participant deleted successfully!")


def participant_menu():
    while True:

        helpers.new_line(2)
        helpers.print_title("==== PARTICIPANT MENU ====")
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
