import os

WIDTH = 90

SEPARATOR = "=" * WIDTH
LINE = "-" * WIDTH


# UI formatting functions

def new_line(count=1):

    for i in range(count):
        print()


def print_separator():
    print(SEPARATOR)


def print_line():
    print(LINE)


# Input validation functions

def is_number(string):

    if not string:
        return False

    digits = "0123456789"

    for character in string:
        if character not in digits:
            return False

    return True


# Screen utility functions

def clear_screen():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Pausing the execution

def pause():
    input("\nPress Enter to continue...")


# Alignment functions

def custom_ljust(text, width, fillchar=" "):

    padding_needed = width - len(text)

    if padding_needed <= 0:
        return text

    return text + (fillchar * padding_needed)


def custom_center(text, width, fillchar=" "):

    padding_needed = width - len(text)

    if padding_needed <= 0:
        return text

    left = padding_needed // 2
    right = padding_needed - left

    return (fillchar * left) + text + (fillchar * right)


def print_title(title):

    print_separator()
    new_line(1)
    print(custom_center(title, WIDTH))
    new_line(1)
    print_separator()


# Sorting functions

def get_sort_key(line):
    return line.split("|")[1]


def bubble_sort(lines):

    for i in range(len(lines)):

        for j in range(len(lines) - 1 - i):

            current_event = get_sort_key(lines[j])
            next_event = get_sort_key(lines[j + 1])

            if current_event > next_event:

                temp = lines[j]
                lines[j] = lines[j + 1]
                lines[j + 1] = temp
