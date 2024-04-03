from app import db

class CarModel(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    make = db.Column(db.String, nullable=False)
    sales = db.relationship("SaleReceiptModel", back_populates="car_sold", lazy='dynamic')

    def save_car(self):
        db.session.add(self)
        db.session.commit()

    def del_car(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def from_dict(cls, car_dict):
        car = cls()
        for k, v in car_dict.items():
            setattr(car, k, v)
        return car
