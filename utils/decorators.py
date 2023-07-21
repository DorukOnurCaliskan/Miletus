import functools

from errors import bad_request
from utils.fortmat_checks import check_email_format, check_password_format


def verify_registration_data(f):
    @functools.wraps(f)
    def decorated_function(request):

        data = request.get_json() or {}
        if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data or 'password' not in data:
            return bad_request("Uyelik bilgilerini tamamalayarak gönderin")

        if not isinstance(data['name'], str) or len(data['name']) < 1:
            return bad_request("İsim formatı yanlış")

        if any(chr.isdigit() for chr in data['name']):
            return bad_request("İsim formatı yanlış")

        if any(chr.isdigit() for chr in data['surname']):
            return bad_request("Soy İsim formatı yanlış")

        if not isinstance(data['surname'], str) or len(data['name']) < 1:
            return bad_request("Soy İsim formatı yanlış")

        if not isinstance(data['email'], str):
            return bad_request("Email formatı yanlış")

        if not '@' in data['email'] and '.com' in data['email']:
            return bad_request("Email formatı yanlış")

        if not isinstance(data['password'], str):
            return bad_request("Şifre formatı yanlış")

        if not check_email_format(data['email']):
            return bad_request("mail formatı yanlış")

        if not check_password_format(data['password']):
            return bad_request("Şifre formatı yanlış")

        return f(data)

    return decorated_function
