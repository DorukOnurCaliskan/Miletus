import re
from flask import jsonify
from sqlalchemy import null

from app.service import user_service
from errors import bad_request
from utils.fortmat_checks import check_password_format, check_email_format


def validate_user_data(data):
    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data or 'password' not in data:
        return bad_request("Uyelik bilgilerini tamamalayarak gönderin")

    if not isinstance(data['name'], str):
        return bad_request("İsim formatı yanlış")
    if data['name'].isdigit():
        return bad_request("İsim formatı yanlış")

    if not isinstance(data['surname'], str):
        return bad_request("Soy İsim formatı yanlış")
    if data['surname'].isdigit():
        return bad_request("İsim formatı yanlış")

    if not isinstance(data['email'], str):
        return bad_request("Email formatı yanlış")

    if not '@' in data['email'] and '.com' in data['email']:
        return bad_request("Email formatı yanlış")

    if not isinstance(data['password'], str):
        return bad_request("Şifre formatı yanlış")

    if not check_email_format(data['email']):
        return bad_request("Şifre formatı yanlış")

    if not check_password_format(data['password']):
        return bad_request("Şifre formatı yanlış")

    return True


def create_new_user_controller(request):
    data = request.get_json()

    is_user_data_correct = validate_user_data(data)

    if is_user_data_correct is not True:
        return is_user_data_correct

    if user_service.get_user_by_phone_service(data['phone']):
        return bad_request("Üyelik var")

    if user_service.create_user_service(data):
        return jsonify(message="Üyelik Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def get_all_users_controller(request):
    user_list = user_service.get_all_users_service()

    # todo: below line better in service
    if not user_list:
        return jsonify(message="Sisteme kayıtlı kullanıcı bulunamadı")

    return jsonify(user_list)


def get_user_by_id_controller(request):
    # todo:you MUST always check your inputs while data read etc

    client_id = request.args.get('id')
    if client_id:
        if not isinstance(client_id, int):
            return bad_request("Kullanıcı Bullunamadı")

    user = user_service.get_user_by_id_service(client_id)
    if user:
        user_dict = user.to_dict()
        return jsonify(user_dict)
    else:
        return bad_request("Kullanıcı Bullunamadı")


def update_phone_number_controller(user_id, request):
    user = user_service.get_user_by_id_service(user_id)

    data = request.get_json()
    # Alternative for more generic usage
    if user_service.update_phone_number_service_v2(user, data):
        if 'phone' in data:
            return jsonify(message='Phone number updated successfully')
        if 'name' in data:
            return jsonify(message='Name updated successfully')
        if 'surname' in data:
            return jsonify(message='Surname updated successfully')
        if 'email' in data:
            return jsonify(message='Email updated successfully')
        if 'password' in data:
            return jsonify(message='Password updated successfully')
        else:
            return bad_request('girilen data bir şey ifade etmiyor')
    else:
        return bad_request("Failed to update phone number")

    # if user_service.update_phone_number_service(user, data['new_phone']):
    #     return jsonify(message='Phone number updated successfully')
    # else:
    #     return bad_request("Failed to update phone number")


def add_n_test_users_controller(request):
    data = request.get_json()
    for user_data in data['users']:
        is_user_data_correct = validate_user_data(user_data)

        if is_user_data_correct is not True:
            print("Girilen kullanıcıların eksik bilgileri var")

        if user_service.get_user_by_phone_service(user_data['phone']):
            print("Üyelik var")
        else:
            if user_service.create_user_service(user_data):
                print("Üyelik başarılı")
            else:
                print("System error")

    return jsonify(message="Olmayan Üyelikler eklendi")


def delete_user_by_phone_number_controller(request):
    data = request.get_json()
    if 'phone' not in data:
        return bad_request("Telefon numarası yok")

    if user_service.delete_user_by_phone_number_service(data['phone']):
        return jsonify(message='User deleted successfully')
    else:
        return bad_request("Failed to delete user")


def login_controller(request):
    data = request.get_json() or {}

    # TODO: check all fields and required format

    if 'email' not in data and 'password' not in data:
        return bad_request("Mıssing Fields")

    email = data['email']
    password = data['password']
    # TODO: need format control

    # IF everything fine lets go

    token = user_service.auth_user_service(email, password)
    if not token:
        return bad_request("Kullanıcı Bulunamadı")
    return jsonify(access_token=token)


def logout_controller(user_id,request):
    data = request.get_json() or {}
    user = user_service.get_user_by_id_service(user_id)
    if not user:
        return bad_request('Kullanıcı Yok')
    else:
        user.token = None
        user.token_expiration = None
        return jsonify('Kullanıcı Silindi')

