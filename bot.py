import asyncio
import logging
from aiogram import Bot, Dispatcher
from Config_data.config import Config, load_config, get_tortoise_config
from handlers import other_handlers

import asyncio
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from db_info.models import Users  # Импортируем вашу модель


app = FastAPI()

tortoise_config = get_tortoise_config()  # Получаем конфигурацию

register_tortoise(
    app,
    config=tortoise_config,
    generate_schemas=True,
    add_exception_handlers=True,
)
async def main() -> None:
  logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s:%(lineno)d #%(levelname)-8s '
    '[%(asctime)s)] - %(name)s - %(message)s'
  )
  logger.info('Starting fitness')
  # await Tortoise.init(
  #       db_url=tortoise_config["connections"]["default"],  # Используем URL из конфигурации
  #       modules={'models': ['db_info.models']},  # Указываем, где находятся ваши модели
  #   )
  # await Tortoise.generate_schemas()
  logger.info('Tortoise started')

  config: Config = load_config()


  bot: Bot = Bot(token=config.tg_bot.token)
  dp: Dispatcher = Dispatcher()

  dp.include_router(other_handlers.router)
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)
  # await Tortoise.close_connections()
  logger.info('Tortoise closed')


logger = logging.getLogger(__name__)

if __name__ == '__main__':
  asyncio.run(main())