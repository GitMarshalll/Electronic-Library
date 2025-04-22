import sqlite3
from MOZES.config import DB_FILE

# 📂 SQLite BAZASINI YARATISH
def connect():
    return sqlite3.connect(DB_FILE, check_same_thread=False)
