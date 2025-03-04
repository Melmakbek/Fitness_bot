from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)  # Первичный ключ
    username = fields.CharField(max_length=255, unique=True) # Unique username

    class Meta:
        table = "users_table"  #  Здесь мы явно указываем имя таблицы