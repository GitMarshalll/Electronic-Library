from MOZES.database.connection import connect


def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, phone FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def save_user(user_id, username, phone):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_id, username, phone) VALUES (?, ?, ?)", (user_id, username, phone))
    conn.commit()
    conn.close()

def update_user(user_id, username, phone):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = ?, phone = ? WHERE user_id = ?", (username, phone, user_id))
    conn.commit()
    conn.close()

# Kitoblar ro'yxatini olish
def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM files ORDER BY name ASC")
    books = cursor.fetchall()
    conn.close()
    return books







