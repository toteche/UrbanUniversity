import sqlite3

DB_PATH = "products.db"

# Создание таблицы Products, если она не существует
def initiate_db():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()
    connection.close()

# Получение всех записей из таблицы Products
def get_all_products():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products

# добавление продуктов в таблицу
def add_products(title, description, price):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO Products (title, description, price)
    VALUES (?, ?, ?)
    ''', (title, description, price))
    connection.commit()
    connection.close()