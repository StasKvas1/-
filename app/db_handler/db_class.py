import sqlite3
import datetime

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('database.db')
        print('подключение произошло успешно!')
    except sqlite3.Error as e:
        print(f'ошибка: {e}')
    return connection

def create_user(user_id: int,
                full_name: str = None):
    conn = create_connection()
    cursor = conn.cursor()

    find_user ='''SELECT * FROM users WHERE user_id = ?'''

    cursor.execute(find_user, (user_id,))
    user = cursor.fetchone()

    if user:
        print('пользователь уже существует')
        return False
    
    create_at = datetime.datetime.now()
    update_at = datetime.datetime.now()
    balance = 0

    create_user = '''INSERT INTO users (user_id, full_name, balance,create_at,update_at)
    VALUES (?,?,?,?,?)'''
    cursor.execute(create_user, (user_id, full_name,
                                 balance,create_at,update_at))
    conn.commit()
    return True
# create_user(1, 'лошок')
create_user(1, 'шпиониро голубиро')