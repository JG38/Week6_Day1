from flask import request
from flask.views import MethodView
from flask_smorest import abort
from schemas import CarSchema, CarWithSaleReceiptSchema
from . import bp
from db import cars
from models.car_model import CarModel

@bp.route('/car', methods=['GET', 'POST'])
class CarList(MethodView):

    @bp.response(200, CarWithSaleReceiptSchema(many=True))
    def get(self):
        return CarModel.query.all()

    @bp.arguments(CarSchema)
    @bp.response(201, CarSchema)
    def post(self, data):
        try:
            car = CarModel()
            car.from_dict(data)
            car.save_car()
            return car
        except:
            abort(400, message='Forgot to add make and model!')


@bp.route('/car/<int:id>', methods=['GET', 'PUT', 'DELETE'])
class Car(MethodView):

    @bp.response(200, CarWithSaleReceiptSchema)
    def get(self, id):
        car = CarModel.query.get(id)
        if car:
            return car
        else:
            abort(400, message='Invalid car id')

    @bp.arguments(CarSchema)
    @bp.response(200, CarWithSaleReceiptSchema)
    def put(self, data, id):
        car = CarModel.query.get(id)
        if car:
            car.from_dict(data)
            car.save_car()
            return car
        else:
            abort(400, message='Invalid car id')

    def delete(self, id):
        car = CarModel.query.get(id)
        if car:
            car.del_car()
            return {'message': f'Car: {car.make} {car.model} deleted'}
        else:
            abort(400, message='Invalid car id')
