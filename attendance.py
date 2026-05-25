import participants
import helpers


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


def mark_attendance():
    '''
    Records attendance of a participant
    '''

    file = open("participants.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No participants available.")
        return

    participants.view_participants()

    choice = input("Enter the participant number: ")
    if not helpers.is_number(choice):
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

    file = open("attendance.txt", "a")
    file.write(participant + "|" + status.title() + "\n")
    file.close()
    print("Attendance recorded successfully!")


def view_attendance():
    '''
    Displays all attendance records
    '''

    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()

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
