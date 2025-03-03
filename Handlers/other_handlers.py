from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F, Bot



router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
  await message.answer('HI', parse_mode = 'HTML')


@router.message(F.text=='HI BOT')
async def hi(message: Message, bot: Bot):
  await bot.send_message(message.from_user.id, 'HI USER')