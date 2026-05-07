from events import view_events


def register_participant():
    '''
    Registers a participant to an existing event
    '''
    with open("events.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No events available.")
        return

    view_events()

    choice = input("Enter the event number to register for: ")

    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    participant_name = input("Enter participant name: ")

    if not participant_name.strip():
        print("Invalid name.")
        return

    selected_event = lines[choice - 1].strip()

    with open("participants.txt", "a") as file:
        file.write(participant_name + "|" + selected_event + "\n")

    print("Participant registered successfully!")


def view_participants():
    '''
    Displays all participants from participants.txt
    '''
    with open("participants.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No participants found.")
        return

    print("PARTICIPANT LIST")

    for i, line in enumerate(lines):
        line = line.strip()
        parts = line.split("|")

        if len(parts) >= 4:
            participant_name = parts[0].strip()
            event_name = parts[1].strip()
            date = parts[2].strip()
            venue = parts[3].strip()

            print(str(i+1) + ". " + participant_name + " | " +
                  event_name + " | " + date + " | " + venue)
        else:
            print("Skipped invalid data.")
