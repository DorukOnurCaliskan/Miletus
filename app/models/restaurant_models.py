from app import db


class Restaurant(db.Model):
    __tablename__ = 'Restaurant'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(40), nullable=False)
    restaurant_address = db.Column(db.String(40), nullable=False, unique=True)
    restaurant_type = db.Column(db.String(40), nullable=False)
    restaurant_opening_hour = db.Column(db.Integer, nullable=False)
    restaurant_closing_hour = db.Column(db.Integer, nullable=False)
    restaurant_status = db.Column(db.String(40), nullable=False)
    products = db.relationship('Product', backref='Product')

    def to_dict(self):
        data = {
            'restaurant_id': self.restaurant_id,
            'restaurant_name': self.restaurant_name,
            'restaurant_address': self.restaurant_address,
            'restaurant_type': self.restaurant_type,
            'restaurant_opening_hour': self.restaurant_opening_hour,
            'restaurant_closing_hour': self.restaurant_closing_hour,
            'restaurant_status': self.restaurant_status,
        }
        return data

    def from_dict_alternative(self, data):
        for field in ['restaurant_name', 'restaurant_address', 'restaurant_opening_hour', 'restaurant_closing_hour',
                      'restaurant_type', 'restaurant_status']:
            if field in data:
                setattr(self, field, data[field])


class Product(db.Model):
    __tablename__ = 'Product'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False, unique=True)
    product_price = db.Column(db.Integer, nullable=False)
    discount_amount = db.Column(db.Integer, nullable=False)
    product_status = db.Column(db.String(40), nullable=False) # TODO: boolean olacak
    #product_status = db.Column(db.Boolean, default=False) #Örnek
    product_stock = db.Column(db.Integer, default=0)  #stock
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurant.restaurant_id'))

    def to_dict(self):
        data = {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price,
            'discount_amount': self.discount_amount,
            'product_status': self.product_status,
            'product_stock': self.product_stock,
            'restaurant_id': self.restaurant_id,
        }
        return data

    def from_dict_alternative(self, data):
        for field in ['product_name', 'product_price', 'discount_amount',
                      'product_status', 'product_stock']:
            if field in data:
                setattr(self, field, data[field])
