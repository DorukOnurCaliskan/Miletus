from app import db

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone
        }
        return data





