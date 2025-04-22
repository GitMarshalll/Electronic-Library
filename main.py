import logging
from aiogram.utils import executor
from handlers import register_handlers
from database.schema import init_db
from bot import dp

# Log sozlamalari
logging.basicConfig(level=logging.INFO)



# Baza yaratish
init_db()

def main():
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()