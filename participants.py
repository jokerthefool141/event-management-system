import events
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

    participants.view_participants()

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
