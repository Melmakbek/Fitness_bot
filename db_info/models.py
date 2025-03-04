from tortoise import fields, models

class User(models.Model):
  id = fields.IntField(pk=True)
  tg_id = fields.BigIntField(unique=True)
  username = fields.CharField(max_length=255, null=True)

  def __str__(self):
    return f"(@{self.username})- {self.tg_id}"