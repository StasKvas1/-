from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.keyboards.all_kb import main_kb, create_spec_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('запуск сообщения по команде /start используя фильтр CommandStart()',
    replay_markup=main_kb(message.from_user.id))

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('запуск сообщения по команде /start_2 используя фильтр Command()',
                         reply_markup=create_spec_kb())
