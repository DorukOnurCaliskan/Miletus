from flask import jsonify

from app.service import restaurant_service
from errors import bad_request
from utils.decorators import verify_restaurant_data, verify_product_data


@verify_restaurant_data
def create_new_restaurant_controller(data):
    if restaurant_service.create_new_restaurant_service(data):
        return jsonify(message="restoran Üyelik Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def edit_restaurant_controller(request):
    data = request.get_json()
    # Alternative for more generic usage
    result_data = {}
    restaurant = restaurant_service.get_restaurant_by_id_service(data['restaurant_id'])
    if restaurant_service.edit_restaurant_service(restaurant, data):
        for field in data:
            if field == "restaurant_name":
                result_data['restaurant_name'] = "updated"
            if field == "restaurant_address":
                result_data['restaurant_address'] = "updated"
            if field == "restaurant_type":
                result_data['restaurant_type'] = "updated"
            if field == "restaurant_opening_hour":
                result_data['restaurant_opening_hour'] = "updated"
            if field == "restaurant_closing_hour":
                result_data['restaurant_closing_hour'] = "updated"
            if field == "restaurant_status":
                result_data['restaurant_status'] = "updated"
        return jsonify(result_data)
    else:
        return bad_request("Failed to update phone number")


@verify_product_data
def add_product_controller(data):
    if restaurant_service.add_product_service(data):
        return jsonify(message="Ürün girme Başarılı")
    else:
        return bad_request("SYSTEM ERROR")


def edit_product_controller(request):
    data = request.get_json()
    # Alternative for more generic usage
    result_data = {}
    product = restaurant_service.get_product_by_id_service(data['product_id'])
    if restaurant_service.edit_product_service(product, data):
        for field in data:
            if field == "product_name":
                result_data['product_name'] = "updated"
            if field == "product_price":
                result_data['product_price'] = "updated"
            if field == "discount_amount":
                result_data['discount_amount'] = "updated"
            if field == "product_status":
                result_data['product_status'] = "updated"
            if field == "product_stock":
                result_data['product_stock'] = "updated"
        return jsonify(result_data)
    else:
        return bad_request("Failed to update data")


def get_all_restaurant_controller(request):
    restaurant_list = restaurant_service.get_all_restaurant_service()

    # todo: below line better in service
    if not restaurant_list:
        return jsonify(message="Sisteme kayıtlı restoran bulunamadı")

    return jsonify(restaurant_list)
