from marshmallow import Schema, fields

class SaleReceiptSchema(Schema):
    id = fields.Str(dump_only=True)
    condition = fields.Str(required=True)
    color = fields.Str(required=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    salesman = fields.Str(required=True)
    sale_id = fields.Int(required=True)


class CarSchema(Schema):
    id = fields.Str(dump_only=True)
    make = fields.Str(required=True)
    model = fields.Str(required=True)


class SaleReceiptWithCarSchema(SaleReceiptSchema):
    car_sold = fields.Nested(CarSchema)


class CarWithSaleReceiptSchema(CarSchema):
    sales = fields.List(fields.Nested(SaleReceiptSchema), dump_only=True)
