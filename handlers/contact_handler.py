from aiogram import types
from MOZES.database.schema import get_user_by_id, save_user, update_user
from MOZES.keyboards.main_menu import main_menu
async def contact_handler(message: types.Message):
    # Foydalanuvchi telefon raqamini yuborganda
    user_id = message.from_user.id
    username = message.from_user.username
    phone = message.contact.phone_number

    user = get_user_by_id(user_id)

    if user:
        db_user_id, db_username, db_phone = user
        if db_username != username or db_phone != phone:
            update_user(user_id, username, phone)
            await message.answer("Ma'lumotlaringiz yangilandi ✅", reply_markup=main_menu())
        else:
            await message.answer("Siz ro'yxatdan o'tgansiz. 👌", reply_markup=main_menu())
    else:
        save_user(user_id, username, phone)
        await message.answer("Raqamingiz qabul qilindi! 👏", reply_markup=main_menu())

