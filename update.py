import participants
import events
import input_validation as valid


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

    participants.view_participants()

    choice = input("Enter the participant number to update: ")
    if not valid.is_number(choice):
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    current = lines[choice - 1].strip().split("|")
    print("Current Name : " + current[0].strip())
    print("Current Event: " + current[1].strip() + " | " +
          current[2].strip() + " | " + current[3].strip())

    new_name = input("Enter new participant name: ").strip()
    if not new_name:
        print("Invalid input. Name cannot be empty.")
        return

    file = open("events.txt", "r")
    event_lines = file.readlines()
    file.close()

    if len(event_lines) == 0:
        print("No events available to assign.")
        return

    events.view_events()

    new_event_choice = input(
        "Enter the new event number for this participant: ")
    if not valid.is_number(new_event_choice):
        print("Invalid selection.")
        return

    new_event_choice = int(new_event_choice)
    if new_event_choice < 1 or new_event_choice > len(event_lines):
        print("Invalid selection.")
        return

    new_event = event_lines[new_event_choice - 1].strip()

    lines[choice - 1] = new_name + "|" + new_event + "\n"

    file = open("participants.txt", "w")
    file.writelines(lines)
    file.close()

    print("Participant updated successfully!")

