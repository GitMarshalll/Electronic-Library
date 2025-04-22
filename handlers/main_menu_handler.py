# main_menu_handler.py
from aiogram import types
from MOZES.keyboards.main_menu import main_menu  # Asosiy menyu tugmalari
from MOZES.bot import bot

async def main_menu_handler(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        "Asosiy menyu:",  # Menyu matni
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=main_menu()  # Asosiy menyu tugmalari
    )