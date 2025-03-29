import sqlite3

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

    if not user:
        create_user = '''INSERT INTO users (user_id, full_name, reg_date)
        VALUES (?,?, datetime('now'))'''
        cursor.execute(create_user, (user_id, full_name))
        conn.commit()
        return user
create_user(1, 'лошок')