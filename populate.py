from crud_functions import initiate_db, add_products
from faker import Faker

# Инициализируем Faker
fake = Faker()

# Инициализируем базу данных
initiate_db()

# Генерация случайных продуктов
def populate_products(n=10):
    for _ in range(n):
        title = fake.word().capitalize()
        description = fake.text(max_nb_chars=50)
        price = fake.random_int(min=50, max=500)
        add_products(title, description, price)

populate_products(10)

print("Таблица Products успешно заполнена случайными данными")