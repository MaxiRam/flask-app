from marshmallow import fields

from app.ext import ma


class DreamSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    topic = fields.String()
