from tortoise import fields
from tortoise.models import Model


class Log(Model):
    id = fields.BigIntField(pk=True)
    type = fields.IntField()
    data = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
