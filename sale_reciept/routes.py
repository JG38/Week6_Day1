from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4
from . import bp
from schemas import SaleReceiptSchema, SaleReceiptWithCarSchema
from models.sale_receipt_model import SaleReceiptModel
from db import cars, sale_receipts

@bp.route('/sale_receipt', methods=['POST'])
class SaleReceiptList(MethodView):
    
    @bp.response(201, SaleReceiptWithCarSchema)
    @bp.arguments(SaleReceiptSchema)
    def post(self, sale_receipt_data):
        try:
            sale_receipt = SaleReceiptModel()
            sale_receipt.from_dict(sale_receipt_data)

            sale_receipt.save_sale_receipt()

            return sale_receipt
        except Exception as e:
            abort(400, message=f'Sale receipt creation failed: {str(e)}')

    @bp.response(200, SaleReceiptSchema(many=True))
    def get(self):
        return SaleReceiptModel.query.all()

@bp.route('/sale_receipt/<sale_receipt_id>', methods=['GET', 'PUT', 'DELETE'])
class SaleReceipt(MethodView):

    @bp.response(200, SaleReceiptSchema)
    def get(self, sale_receipt_id):
        try: 
            return SaleReceiptModel.query.get(sale_receipt_id)
        except KeyError:
            abort(400, message="Invalid sale receipt id")

    @bp.arguments(SaleReceiptSchema)
    @bp.response(201, SaleReceiptWithCarSchema)
    def put(self, sale_receipt_data, sale_receipt_id):
        sale_receipt = SaleReceiptModel.query.get(sale_receipt_id)
        if not sale_receipt:
            abort(400, message='Sale receipt not found')
        
        if sale_receipt_data['sale_receipt_id'] == sale_receipt.sale_id:
            og_sale_id = sale_receipt.sale_id
            sale_receipt.from_dict(sale_receipt_data)
            sale_receipt.sale_id = og_sale_id

            sale_receipt.save_sale_receipt()
            return sale_receipt

    def delete(self, sale_receipt_id):
        sale_receipt = SaleReceiptModel.query.get(sale_receipt_id)
        if not sale_receipt:
            abort(400, message="Sale receipt not found")
        
        sale_receipt.del_sale_receipt()
        return {'message': f'Sale receipt {sale_receipt_id} deleted'}, 200
