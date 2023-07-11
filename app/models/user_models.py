from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_manager, login_required, logout_user, current_user


class User(db.Model,UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(14), nullable=False, unique=True)  # unique=True
    email = db.Column(db.String(40), nullable=False, unique=True)  # unique=True
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
            'email': self.email,
        }
        return data

    def from_dict(self, data):
        user = self
        user.id = data.get('id')
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.phone = data.get('phone')
        user.email = data.get('email')
        user.password = data.get('password')
        return user
