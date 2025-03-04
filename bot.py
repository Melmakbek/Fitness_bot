import asyncio
import logging
from aiogram import Bot, Dispatcher
from Config_data.config import Config, load_config
from handlers import other_handlers
from db_info.db import init_tortoise, close_tortoise
from db_info.models import User
import asyncio

async def main() -> None:
  logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
    '[%(asctime)s)] - %(name)s - %(message)s'
  )
  logger.info('Starting fitness')

  config: Config = load_config()


  bot: Bot = Bot(token=config.tg_bot.token)
  dp: Dispatcher = Dispatcher()

  dp.include_router(other_handlers.router)
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

  async def on_startup():
    await init_tortoise()
    # Generate the schema here or using Aerich
    # await Tortoise.generate_schemas()
    print("Tortoise ORM initialized.")


  async def on_shutdown():
    await close_tortoise()
    print("Tortoise ORM closed.")
logger = logging.getLogger(__name__)

if __name__ == '__main__':
  asyncio.run(main())