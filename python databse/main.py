import sqlite3 

db=sqlite3.connect('users.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)""")
db.commit()

def reg():
    login=input('Login: ')
    password=input('Password: ')
    cur.execute(f"SELECT login FROM  users WHERE login='{login}'")
    if cur.fetchone() is None:
        cur.execute("""INSERT INTO users VALUES(?,?)""", (login,password))
        db.commit()
    else: 
        print('Такий користувач уже зареєстрований! ')
        for value in cur.execute(f"SELECT * FROM users WHERE login='{login}'"):
            print(value)


def prnt():
    for value in cur.execute("SELECT * FROM users"):
        print(value)


def adj():
    login = input('Введіть логін користувача якому хочете змінити пароль: ')
    cur.execute(f"SELECT login FROM  users WHERE login='{login}'")
    if cur.fetchone() is None:
        print('Користувачів не знайдено!')
        return
    password = input('Введіть новий пароль: ')
    cur.execute(f"""
    UPDATE users SET password = '{password}' WHERE login ='{login}'
    """)
    db.commit()
    for value in cur.execute(f"SELECT * FROM users WHERE login='{login}' "):
        print(value)


def dlt():
    login = input('Введіть логін користувача якого хочете видалити: ')
    cur.execute(f"SELECT login FROM  users WHERE login='{login}'")
    if cur.fetchone() is None:
        print('Користувачів не знайдено!')
        return
    cur.execute(f"DELETE from users WHERE login='{login}'")
    db.commit()
    prnt()


while True:
    print("""
    1 - зареструвати нового користувача
    2 - вивести всю шнформацію в базі даних
    3 - редагувати інформацію про користувача
    4 - видалити користувача
    5 - вихід 
    """)
    det = int(input())
    if det == 1:
        reg()
    elif det == 2:
        prnt()
    elif det == 3:
        adj()
    elif det == 4:
        dlt()
    elif det == 5:
        break
    else: print("Невірні дані")