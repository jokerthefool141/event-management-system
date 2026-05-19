def is_number(string):

    if not string:
        return False

    digits = "0123456789"

    for characters in string:
        if characters not in digits:
            return False

    return True
