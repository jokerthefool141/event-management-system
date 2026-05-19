def create_event():
    # file = open("events.txt")
    # print(file.readline(1)
    '''
    Lists / adds a new event

    '''
    print("                ===== EVENT MENU =====\n")
    print("=" * 55)
    print()
    event_name = input(
        "Enter the event name you want to add: ").strip().title()
    print()
    print("-" * 55)
    print()
    date = input("Enter event date: ").strip().title()
    print()
    print("-" * 55)
    print()
    venue = input("Enter event venue: ").strip().title()
    print()
    print("=" * 55)
    if not event_name or not date or not venue:
        print("\nFields cannot be empty. Please try again.\n")
        print("=" * 55)
    else:
        file = open("events.txt", "a")
        file.write(event_name + "|" + date + "|" + venue + "\n")
        file.close()
        print("\nEvent added successfully!\n")
        print("=" * 55)


def view_events():
    '''
    Displays all events from events.txt
    '''
    file = open("events.txt", "r")
    lines = file.readlines()
    file.close()
    if len(lines) == 0:
        print("No events found (file is empty).")
        return

    print("                ===== EVENT LIST =====\n")
    print("=" * 55)
    print()

    for i in range(len(lines)):
        line = lines[i].strip()
        parts = line.split("|")

        if len(parts) >= 3:
            event_name = parts[0].strip()
            date = parts[1].strip()
            venue = parts[2].strip()
            print("-" * 55)
            print(str(i+1) + ". " + event_name + " | " + date + " | " + venue)
        else:
            print("Skipped invalid data.")

    print("-" * 55)
