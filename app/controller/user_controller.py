from flask import jsonify
from app.service import user_service
from errors import bad_request


def validate_user_data(data):
    # todo: add password check

    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data or 'password' not in data:
        return bad_request("Uyelik bilgilerini tamamalayarak gönderin")

    # TODO: do not accept any numbers in name
    #TODO: example: HAKAN1
    if not isinstance(data['name'], str):
        return bad_request("İsim formatı yanlış")

    #TODO: example: Biri2
    #TODO: do not accept any numbers in surname
    if not isinstance(data['surname'], str):
        return bad_request("Soy İsim formatı yanlış")

    # TODO: make email check more complex,
    # TODO: do not accept hakanhakan
    # TODO: check  @ and .com is in mail
    if not isinstance(data['email'], str):
        return bad_request("Soy İsim formatı yanlış")

    #TODO: make password controller more complex
    #TODO: example: Password must be at least 8 chars, at least one capital char and one special char
    if not isinstance(data['password'], str):
        return bad_request("Soy İsim formatı yanlış")

    return True


def create_new_user_controller(request):
    data = request.get_json()

    # todo. you have to add format controller for all fields
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
            return "Kullanıcı Bulunamadı"

    user = user_service.get_user_by_id_service(client_id)
    if user:
        user_dict = user.to_dict()
        return jsonify(user_dict)
    else:
        return bad_request("Kullanıcı Bullunamadı")


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


    #TODO: check all fields and required format

    if 'email' not in data:
        return bad_request("Mıssing Fields")

    email = data['email']
    password = data['password']
    #TODO: need format control

    #IF everything fine lets go

    token = user_service.auth_user_service(email, password)
    if not token:
        return bad_request("Kullanıcı Bulunamadı")
    return jsonify(access_token=token)