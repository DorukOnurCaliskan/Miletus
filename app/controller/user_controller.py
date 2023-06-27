import sys

from flask import jsonify
from app.service import user_service
from errors import bad_request


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
    users = user_service.get_all_users_service()
    user_list = [user.to_dict() for user in users]  # Convert users to a list of dictionaries
    return jsonify(user_list)


def get_user_by_id_controller(request):
    user = user_service.get_user_by_id_service(request.args.get('id'))
    user_dict = user.to_dict()
    return jsonify(user_dict)


def update_phone_number_controller(request):
    data = request.get_json()
    if 'phone' not in data:
        return bad_request("Telefon numarası gerekli")

    if user_service.update_phone_number_service(data['phone'], data['new_phone']):
        return jsonify(message='Phone number updated successfully')
    else:
        return bad_request("Failed to update phone number")


def add_n_test_users_controller(request):
    data = request.get_json()
    for user_data in data['users']:
        is_user_data_correct = validate_user_data(user_data)

        if is_user_data_correct is not True:
            print("Girilen kullanıcıların eksik bilgileri var var")

        if user_service.get_user_by_phone_service(user_data['phone']):
            print("Üyelik var")
        else:
            if user_service.create_user_service(user_data):
                print("Üyelik başarılı")
            else:
                print("System error")

    return jsonify(message="Olmayan Üyelikler eklendi")

def validate_user_data(data):
    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data:
        return bad_request("Uyelik bilgilerini tamamalayarak gönderin")

    if not isinstance(data['name'], str):
        return bad_request("İsim formatı yanlış")

    if not isinstance(data['surname'], str):
        return bad_request("Soy İsim formatı yanlış")
    return True
