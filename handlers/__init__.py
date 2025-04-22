from aiogram import types
from aiogram.dispatcher import Dispatcher
from .contact_handler import contact_handler
from .start import start
from .e_book_handler import ebook_menu, ask_book_name
from .main_menu_handler import main_menu_handler

from MOZES.handlers.e_library_list_handler import list_books
from MOZES.handlers.e_library_callback import go_to_library



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(contact_handler, content_types=types.ContentTypes.CONTACT)

    # Callbacks
    dp.register_callback_query_handler(ebook_menu, text="ebooks")
    dp.register_callback_query_handler(ask_book_name, text="ebook_search_book")
    dp.register_callback_query_handler(main_menu_handler, text="main_menu")
    dp.register_callback_query_handler(go_to_library, text="e_books")
    dp.register_callback_query_handler(list_books, text="list_books")

