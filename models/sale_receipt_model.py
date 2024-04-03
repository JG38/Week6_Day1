from datetime import datetime
from app import db

class SaleReceiptModel(db.Model):
    __tablename__ = 'sale_receipts'

    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.String, nullable=True)
    color = db.Column(db.String, nullable=True)
    make = db.Column(db.String, nullable=True)
    model = db.Column(db.String, nullable=True)
    salesman = db.Column(db.String, nullable=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)

    car_sold = db.relationship("CarModel", back_populates='sales')

    def from_dict(self, a_dict):
        self.condition = a_dict.get('condition')
        self.color = a_dict.get('color')
        self.make = a_dict.get('make')
        self.model = a_dict.get('model')
        self.salesman = a_dict.get('salesman')
        self.sale_id = int(a_dict.get('sale_id'))

    def save_sale_receipt(self):
        db.session.add(self)
        db.session.commit()

    def del_sale_receipt(self):
        db.session.delete(self)
        db.session.commit()
