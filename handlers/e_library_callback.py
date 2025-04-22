from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from e_library_list_handler import list_books


async def go_to_library(callback_query: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("📚 Mavjud kitoblar ro'yxati", callback_data="list_books")
    )
    await callback_query.message.edit_text("Kutubxona bo'limiga xush kelibsiz!", reply_markup=keyboard)