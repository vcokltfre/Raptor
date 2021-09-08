from tortoise import fields
from tortoise.models import Model


class Guild(Model):
    id = fields.BigIntField(pk=True)
    name = fields.TextField()
    owner_id = fields.BigIntField()
    icon_url = fields.TextField()
