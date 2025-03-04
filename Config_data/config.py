from __future__ import annotations

import os
from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
  token: str


@dataclass
class Config:
  tg_bot: TgBot


def load_config(path: str | None = None) -> Config:

  env: Env = Env()
  env.read_env(path)

  return Config(
    tg_bot = TgBot(
      token = env('BOT_TOKEN')
    )
  )

def get_database_url():
    """Получает URL базы данных из переменной окружения или предоставляет значение по умолчанию."""
    return os.environ.get(
        "DATABASE_URL",
        "postgres://postgres:postgres@localhost:5432/postgres",  # Значение по умолчанию для разработки
    )


def get_tortoise_config():
    """Возвращает конфигурацию Tortoise-ORM."""
    database_url = get_database_url()
    return {
        "connections": {"default": database_url},
        "apps": {
            "models": {
                "models": ["db_info.models"],  # Укажите, где находятся ваши модели
                "default_connection": "default",
            },
        },
    }