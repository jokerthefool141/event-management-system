def create_event():
    # file = open("events.txt")
    # print(file.readline(1)
    '''
    Lists / adds a new event

    '''
    event_name = input("Enter the event name you want to add: ")
    date = input("Enter event date: ")
    venue = input("Enter event venue: ")
    if not event_name or not date or not venue:
        print("Fields cannot be empty. Please try again.")
    else:
        file = open("events.txt", "a")
        file.write(event_name + "|" + date + "|" + venue + "\n")
        file.close()
        print("Event added successfully!")


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

    print("EVENT LIST")

    for i, line in enumerate(lines):
        line = line.strip()
        parts = line.split("|")

        if len(parts) >= 3:
            event_name = parts[0].strip()
            date = parts[1].strip()
            venue = parts[2].strip()
            print(str(i+1) + ". " + event_name + " | " + date + " | " + venue)
        else:
            print("Skipped invalid data.")
