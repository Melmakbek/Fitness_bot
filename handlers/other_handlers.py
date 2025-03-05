from aiogram import Router
from aiogram.types import Message
from aiogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton, User, Chat,
    CallbackQuery,
)
from aiogram.filters import CommandStart
from aiogram import F, Bot
from db_info.models import Users


TRAININGS = "trainings"
STEP1_COLLAPSE_CB = "collapse"
MY_TRAININGS = "my_trainings"

router: Router = Router()

@router.message(CommandStart())
async def step1(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Упражнения",
                             callback_data=TRAININGS),
        InlineKeyboardButton(text="Мои упражнения", callback_data=MY_TRAININGS),
    ]])

    # await process_start_command(Message)

    await message.answer(
        f"Hello, {message.from_user.username}. \n\n"
        "Extended mode is off.",
        reply_markup=keyboard,
    )
# async def process_start_command(message: Message):
#   try:
#     # Проверяем, существует ли пользователь по telegram_id
#     user, created = await Users.get_or_create(id=message.from_user.id, defaults={'username': message.from_user.username})
#     if created:
#       await message.reply("Добро пожаловать! Вы зарегистрированы.")
#     else:
#       await message.reply("Вы уже зарегистрированы!")
#   except Exception as e:
#     print(f"Ошибка при работе с базой данных: {e}")
#     await message.reply("Произошла ошибка при регистрации.")


@router.message(F.text=='HI BOT')
async def hi(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, 'HI USER')