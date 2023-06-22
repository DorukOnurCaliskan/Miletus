from flask import jsonify, request
from app import app, db
from app.api import bp
from app.models.user_models import User


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User.from_dict(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201
