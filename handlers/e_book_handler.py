from aiogram import types
from MOZES.keyboards.e_book_menu import get_ebook_keyboard, get_back_keyboard
from MOZES.bot import bot


async def ebook_menu(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        "📚 Elektron kitoblar bo‘limi:",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=get_ebook_keyboard()
    )


async def ask_book_name(callback_query: types.CallbackQuery):
    await bot.edit_message_text(
        "Kitob nomini kiriting:",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=get_back_keyboard()
    )