from participants import view_participants


def delete_participant():
    '''
    Deletes an existing participant
    '''

    with open("participants.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No participants to delete.")
        return

    view_participants()

    choice = input("Enter the participant number to delete: ")
    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    lines.pop(choice - 1)

    with open("participants.txt", "w") as file:
        file.writelines(lines)

    print("Participant deleted successfully!")


def mark_attendance():
    '''
    Records attendance of a participant
    '''

    with open("participants.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No participants available.")
        return

    view_participants()

    choice = input("Enter the participant number: ")
    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice < 1 or choice > len(lines):
        print("Invalid selection.")
        return

    participant = lines[choice - 1].strip()

    status = input("Enter attendance (Present/Absent): ").strip()

    if status.lower() != "present" and status.lower() != "absent":
        print("Invalid attendance status.")
        return

    with open("attendance.txt", "a") as file:
        file.write(participant + "|" + status.title() + "\n")

    print("Attendance recorded successfully!")


def view_attendance():
    '''
    Displays all attendance records
    '''

    with open("attendance.txt", "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No attendance records found.")
        return

    print("\n===== ATTENDANCE RECORDS =====")

    count = 1

    for line in lines:
        record = line.strip().split("|")

        print(
            str(count) + ". " +
            record[0] + " | " +
            record[1] + " | " +
            record[2] + " | " +
            record[3] + " | " +
            record[4]
        )

        count += 1
