import re

from errors import bad_request


def check_password_format(passwd):
    if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$%^&+=]).{8,}$', passwd):
        return True
    else:
        return False