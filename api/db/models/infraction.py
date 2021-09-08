from tortoise import fields
from tortoise.models import Model


class Infraction(Model):
    id = fields.BigIntField(pk=True)
    type = fields.IntField()
    user_id = fields.BigIntField(index=True)
    user_name = fields.CharField(max_length=255)
    mod_id = fields.BigIntField(index=True)
    mod_name = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    expires_at = fields.DatetimeField(null=True)
    is_expired = fields.BooleanField(default=False)
    is_hidden = fields.BooleanField(default=False)
    metadata = fields.JSONField(null=True)
