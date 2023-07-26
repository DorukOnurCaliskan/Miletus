from app import db


class Order(db.Model):
    __tablename__ = 'Order'
    order_id = db.Column(db.Integer, primary_key=True)
    order_address = db.Column(db.String(40), nullable=False)
    order_status = db.Column(db.String(40), nullable=False)
    rest_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def to_dict(self):
        data = {
            'order_id': self.order_id,
            'order_address': self.order_address,
            'order_status': self.order_status,
            'restaurant_id': self.rest_id,
            'user_id': self.user_id,
        }
        return data

    def from_dict_alternative(self, data):
        for field in ['order_id', 'order_address', 'order_status', 'restaurant_id', 'user_id']:
            if field in data:
                setattr(self, field, data[field])


class Cart(db.Model):
    __tablename__ = 'Cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('Order.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('Product.product_id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.restaurant_id'))

    def to_dict(self):
        data = {
            'cart_id': self.cart_id,
            'product_id': self.product_id,
            'order_id': self.order_id,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id,
        }
        return data

    def from_dict_alternative(self, data):
        for field in ['cart_id', 'product_id','order_id','restaurant_id','user_id']:
            if field in data:
                setattr(self, field, data[field])
