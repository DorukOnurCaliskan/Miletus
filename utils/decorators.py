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

        if not isinstance(data['surname'], str) or len(data['surname']) < 1:
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


def verify_restaurant_data(f):
    @functools.wraps(f)
    def decorated_function(request):

        data = request.get_json() or {}
        if 'restaurant_name' not in data or 'restaurant_address' not in data or 'restaurant_opening_hour' not in data or 'restaurant_closing_hour' not in data or 'restaurant_type' not in data:
            return bad_request("Restoran bilgilerini tamamalayarak gönderin")

        if not isinstance(data['restaurant_name'], str) or len(data['restaurant_name']) < 1:
            return bad_request("Restoran isim formatı yanlış")

        if any(chr.isdigit() for chr in data['restaurant_name']):
            return bad_request("İsim formatı yanlış")

        if any(chr.isdigit() for chr in data['restaurant_address']):
            return bad_request("Adres formatı yanlış")

        if not isinstance(data['restaurant_address'], str) or len(data['restaurant_address']) < 1:
            return bad_request("Adres İsim formatı yanlış")

        if not isinstance(data['restaurant_opening_hour'], int):
            return bad_request("Açılış saat formatı yanlış")

        if not isinstance(data['restaurant_closing_hour'], int):
            return bad_request("Açılış saat formatı yanlış")

        if not isinstance(data['restaurant_type'], str):
            return bad_request("Tip formatı yanlış")

        return f(data)

    return decorated_function

def verify_product_data(f):
    @functools.wraps(f)
    def decorated_function(request):

        data = request.get_json() or {}
        if 'product_name' not in data or 'product_price' not in data or 'discount_amount' not in data:
            return bad_request("Ürün bilgilerini tamamalayarak gönderin")

        if not isinstance(data['product_name'], str) or len(data['product_name']) < 1:
            return bad_request("Ürün isim formatı yanlış")

        if not isinstance(data['product_price'], int):
            return bad_request("Fiyat saat formatı yanlış")

        if not isinstance(data['discount_amount'], int):
            return bad_request("İndirim saat formatı yanlış")


        return f(data)

    return decorated_function
