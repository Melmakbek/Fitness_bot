from tortoise import Tortoise
from tortoise import run_async

TORTOISE_ORM = {
    "connections": {"default": ""},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"], # models - файл с моделями ваших таблиц, а aerich.models - необходим для корректной работы миграций
            "default_connection": "default",
        },
    },
}

async def generate_db_schema():
    await Tortoise.init(
        db_url="postgres://myuser:mysecretpassword@localhost:5432/my_telegram_bot",
        modules={"models": ["models"]},
    )
    # Generate the schema
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()

async def init_tortoise():
    await Tortoise.init(config=TORTOISE_ORM)
    # Optionally, generate the schema here ONLY for the first time
    # await Tortoise.generate_schemas()

async def close_tortoise():
    await Tortoise.close_connections()

if __name__ == 'main':
    run_async(generate_db_schema())