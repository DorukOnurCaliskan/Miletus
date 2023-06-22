from flask import jsonify, request
from app import app, db
from user_models import User


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User.from_dict(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201
