def update_participant():
    '''
    Updates an existing participant's name and event
    '''

    with open("participants.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No participants to update.")
        return

    view_participants()

    choice = input("Enter the participant number to update: ")
    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    current = lines[choice - 1].strip().split("|")
    print("Current Name : " + current[0].strip())
    print("Current Event: " + current[1].strip() + " | " + current[2].strip() + " | " + current[3].strip())

    new_name = input("Enter new participant name: ").strip()
    if not new_name:
        print("Invalid input. Name cannot be empty.")
        return

    with open("events.txt", "r") as file:
        event_lines = file.readlines()

    if len(event_lines) == 0:
        print("No events available to assign.")
        return

    view_events()
    new_event_choice = input("Enter the new event number for this participant: ")
    if not new_event_choice.isdigit():
        print("Invalid selection.")
        return

    new_event_choice = int(new_event_choice)
    if new_event_choice < 1 or new_event_choice > len(event_lines):
        print("Invalid selection.")
        return

    new_event = event_lines[new_event_choice - 1].strip()

    lines[choice - 1] = new_name + "|" + new_event + "\n"

    with open("participants.txt", "w") as file:
        file.writelines(lines)

    print("Participant updated successfully!")