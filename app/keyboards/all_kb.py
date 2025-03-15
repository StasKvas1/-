from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [[KeyboardButton(text='о нас'),
                KeyboardButton(text='профиль')]

                [KeyboardButton(text='настроики'),
                KeyboardButton(text='каталог')]]
    keyboard = ReplyKeyboardMarkup(
                keyboard=kb_list,
                resize_keyboard=True,
                one_time_keyboard=True,
                input_field_placeholder='Воспользуитесь меню:'

            )
    
    return keyboard

def create_spec_kb():
      keyboard = ReplyKeyboardMarkup(
                keyboard=kb_list,
                resize_keyboard=True,
                one_time_keyboard=True,
                input_field_placeholder='Воспользуитесь меню:'

            )
      kb_list=[
            [
                  KeyboardButton(text='геопозиция',
                                 request_location=True)
            ],
            [
                  KeyboardButton(text='номер телефона',
                                 request_contact=True)
            ],
      ]