from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Bot
from db_info.models import User



router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
  try:
    # Проверяем, существует ли пользователь по telegram_id
    user, created = await User.get_or_create(telegram_id=message.from_user.id, defaults={'username': message.from_user.username})
    if created:
      await message.reply("Добро пожаловать! Вы зарегистрированы.")
    else:
      await message.reply("Вы уже зарегистрированы!")
  except Exception as e:
    print(f"Ошибка при работе с базой данных: {e}")
    await message.reply("Произошла ошибка при регистрации.")
  await message.answer('HI', parse_mode = 'HTML')


@router.message(F.text=='HI BOT')
async def hi(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, 'HI USER')