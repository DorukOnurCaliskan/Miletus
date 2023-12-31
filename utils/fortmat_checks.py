import re

from errors import bad_request


def check_password_format(passwd):
    if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&+=]).{8,}$', passwd):
        return True
    else:
        return False


def check_email_format(email):
    if re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return True
    else:
        return False
