from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from MOZES.keyboards.main_menu import main_menu
from MOZES.database.schema import get_user_by_id


async def start(message: types.Message):
    user_id = message.from_user.id
    user = get_user_by_id(user_id)
    if user:
        db_user_id, db_username, db_phone = user
        current_username = message.from_user.username

        # Hozircha phone raqamni tekshira olmaymiz, faqat username tekshiramiz
        # Chunki phone faqat contact yuborilganda aniqlanadi
        if db_username != current_username:
            # Username o'zgargan, yangilash kerak. Phone contact handlerda yangilanadi.
            from MOZES.database.schema import update_user
            update_user(user_id, current_username, db_phone)
            await message.answer("Ma'lumotlaringiz yangilandi ✅", reply_markup=main_menu())
        else:
            await message.answer("Xush kelibsiz! 👋", reply_markup=main_menu())
    else:
        # Telefon raqamni so‘raymiz
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        contact_btn = KeyboardButton("📱 Telefon raqamni yuborish", request_contact=True)
        markup.add(contact_btn)
        await message.answer("Iltimos, telefon raqamingizni yuboring:", reply_markup=markup)
