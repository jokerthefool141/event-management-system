import events
import input_validation as valid


def register_participant():
    '''
    Registers a participant to an existing event
    '''
    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No events available.")
        return

    events.view_events()

    choice = input("Enter the event number to register for: ")

    if not valid.is_number(choice):
        print("Invalid event selection.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):
        print("Invalid event selection.")
        return

    participant_name = input("Enter participant name: ").strip()

    if not participant_name:
        print("Invalid name.")
        return

    selected_event = lines[choice - 1].strip()

    file = open("participants.txt", "a")
    file.write(participant_name + "|" + selected_event + "\n")
    file.close()

    print("Participant registered successfully!")


def view_participants():
    '''
    Displays all participants from participants.txt
    '''
    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No participants found.")
        return

    print("\n===== PARTICIPANT LIST =====\n")

    for i in range(len(lines)):
        line = lines[i].strip()
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
