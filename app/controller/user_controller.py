from flask import jsonify

from app.service import user_service
from errors import bad_request


def create_new_user_controller(request):
    data = request.get_json()

    if 'name' not in data or 'surname' not in data or 'phone' not in data or 'email' not in data:
        return bad_request("Uyelik bilgilerini tamamalayarak gönderin")

    if not isinstance(data['name'], str):
        return bad_request("İsim formatı yanlış")

    if not isinstance(data['surname'], str):
        return bad_request("Soy İsim formatı yanlış")

    if user_service.get_user_by_phone_service(data['phone']):
        return bad_request("Üyelik var")

    if user_service.create_user_service(data):
        return jsonify(message="Üyelik Başarılı")
    else:
        return bad_request("SYSTEM ERROR")
