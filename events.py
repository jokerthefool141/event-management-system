import helpers


def create_event():
    # file = open("events.txt")
    # print(file.readline(1)
    '''
    Lists / adds a new event

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
        print("No events found (file is empty).\n")
        return

    helpers.print_title("===== EVENT LIST =====")
    helpers.new_line()

    print(helpers.custom_ljust("No.", 5) +
          helpers.custom_ljust("Event Name", 25) +
          helpers.custom_ljust("Date", 25) +
          helpers.custom_ljust("Venue", 20))

    helpers.new_line()
    helpers.print_line()

    for i in range(len(lines)):
        line = lines[i].strip()
        parts = line.split("|")

        if len(parts) >= 3:
            event_name = parts[0].strip()
            date = parts[1].strip()
            venue = parts[2].strip()

            helpers.new_line()
            print(
                helpers.custom_ljust(str(i + 1), 5) +
                helpers.custom_ljust(event_name, 25) +
                helpers.custom_ljust(date, 25) +
                helpers.custom_ljust(venue, 20)
            )

        else:
            helpers.new_line()
            print("Skipped invalid data.")

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

    if len(lines) == 0:
        print("No events found (file is empty).\n")
        return

    view_events()

    choice = input("\nEnter the event number to remove: ").strip()

    if not helpers.is_number(choice):
        print("Invalid input. Please enter a valid number.")
        helpers.print_separator()
        return

    choice = int(choice)

    if choice < 1 or choice > len(lines):
        print("Please try again.")
        helpers.print_separator()
        return

    removed_event = lines.pop(choice - 1)

    file = open("events.txt", "w")
    file.writelines(lines)
    file.close()

    print("\nEvent removed successfully!\n")
    helpers.print_separator()
