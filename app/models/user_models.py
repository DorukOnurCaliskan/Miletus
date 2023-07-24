import base64
import os
from datetime import datetime, timedelta

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, login_manager, login_required, logout_user, current_user


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(14), nullable=False, unique=True)  # unique=True
    email = db.Column(db.String(40), nullable=False, unique=True)  # unique=True
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    orders = db.relationship('Order', backref='Order')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=60 * 60 * 24 * 7):
        now = datetime.now()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        db.session.commit()
        return self.token

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.now():
            return None
        return user

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
        user.name = data.get('name')
        user.surname = data.get('surname')
        user.phone = data.get('phone')
        user.email = data.get('email')
        user.password = data.get('password')
        return user

    def from_dict_alternative(self, data, is_new=False):
        for field in ['name', 'surname', 'phone', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if is_new:
            setattr(self, 'password', data['password'])

class Order(db.Model):
    __tablename__ = 'Order'
    order_id = db.Column(db.Integer, primary_key=True)
    order_address = db.Column(db.String(40), nullable=False)
    #order_status
    rest_id = db.Column(db.String(40), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(40), nullable=False)
    restaurant_address = db.Column(db.String(40), nullable=False, unique=True)
    #oepning_hour
    #closing hour
    #status

    products = db.relationship('Product', backref='Product')


class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    discount_amount = db.Column(db.Integer, nullable=False)
    #status
    #stock
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.restaurant_id'))



# class Order(db.Model):
#     pass

# class Order(db.Model):
#     pass
