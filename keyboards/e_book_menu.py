from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_ebook_keyboard():
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton("📖 Kitob qidirish", callback_data="ebook_search_book"),
        InlineKeyboardButton("📚 Mavjud kitoblar ro'yxati", callback_data="ebook_list_books"),
        InlineKeyboardButton("🔙 Ortga", callback_data="main_menu")
    )

def get_back_keyboard():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔙 Ortga", callback_data="ebooks")
    )