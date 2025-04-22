from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MOZES.database.schema import get_all_books

async def list_books(callback_query: types.CallbackQuery):
    # Baza orqali kitoblar ro'yxatini olish
    books = get_all_books()

    # Ortga tugmasi
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔙 Ortga", callback_data="ebooks")
    )

    # Kitoblar mavjud bo'lsa, foydalanuvchiga taqdim etish
    if books:
        book_text = "📚 Mavjud kitoblar ro'yxati:\n"
        book_text += "\n".join([book[0] for book in books])  # Kitob nomlarini olish
        await callback_query.message.edit_text(book_text, reply_markup=keyboard)
    else:
        # Kitoblar yo'q bo'lsa
        await callback_query.message.edit_text("Hozircha kitoblar yo'q!", reply_markup=keyboard)