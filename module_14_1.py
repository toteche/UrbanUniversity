import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Users')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
);
''')

for i in range(10):
    cursor.execute(" INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)", (f"{i}", f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

# Обновляем balance у каждой 2-й записи начиная с 1-й на 500
cursor.execute('''
UPDATE Users SET balance = 500 WHERE id % 2 = 1;
''')

# Удаляем каждую 3-ю запись начиная с 1-й
cursor.execute('''DELETE FROM Users WHERE id = 1;''')

cursor.execute('''
DELETE FROM Users WHERE id IN (
    SELECT id FROM (
        SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS row_num FROM Users
    ) WHERE (row_num - 1) % 3 = 0
);
''')

# Выбираем все записи, где возраст не равен 60
cursor.execute("""
SELECT username, email, age, balance FROM Users WHERE age != 60
""")

rows = cursor.fetchall()

# Выводим результат в заданном формате
for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")


connection.commit()
connection.close()


