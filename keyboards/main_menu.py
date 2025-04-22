from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
    InlineKeyboardButton("📚 Elektron kitoblar", callback_data="ebooks"),
        InlineKeyboardButton("🏛 Kutubxona", callback_data="library"),
        InlineKeyboardButton("🎧 Audio kitoblar", callback_data="audiobooks"),
        InlineKeyboardButton("🔍 Izlash", callback_data="search")
    )
    return keyboard