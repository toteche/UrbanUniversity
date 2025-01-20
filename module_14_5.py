import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, get_all_products, is_included, add_user


api = "7739274992:AAHqPdBPfvHfVgCpdaowrc3_kWxHfl4Zdb0"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

IMG_DIR = "img"

# Инициализация базы данных
initiate_db()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

# основное меню
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
reply_keyboard.row(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))
reply_keyboard.row(KeyboardButton("Купить"))
reply_keyboard.row(KeyboardButton("Регистрация"))

# Inline-клавиатура
inline_keyboard = InlineKeyboardMarkup(row_width=1)
inline_keyboard.add(
    InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories"),
    InlineKeyboardButton("Формулы рассчета", callback_data="formulas")
    )

# Функция для команды start
@dp.message_handler(commands=['start'])
async def send_welcome(message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=reply_keyboard)

# Регистрация пользователя
@dp.message_handler(Text(equals="Регистрация", ignore_case=True))
async def sing_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латиницей):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        data = await state.get_data()
        add_user(data['username'], data['email'], age)
        await message.answer("Регистрация завершена! Ваш баланс: 1000.")
        await state.finish()
    except ValueError:
        await message.answer("Возраст должен быть числом. Попробуйте еще раз:")


# Inline меню - Купить
def get_inline_menu():
    inline_keyboard = InlineKeyboardMarkup(row_width=4)

    buttons = [
        InlineKeyboardButton(f"Product{i+1}", callback_data="product_buying")
        for i in range(len(get_all_products()))  # Количество кнопок зависит от записей в bd
    ]
    inline_keyboard.add(*buttons)
    return inline_keyboard

# Функция для отправки списка товаров
async def get_buying_list(message: types.Message):
    products = get_all_products()
    for product in products:
        product_id, title, description, price = product
        product_text = f"Название: {title} | Описание: {description} | Цена: {price}"
        await message.answer(product_text)

        # Генерируем путь к файлу
        image_path = os.path.join(IMG_DIR, f"{product_id:02}.png")

        # Проверяем, существует ли файл, перед отправкой
        if os.path.exists(image_path):
            with open(image_path, "rb") as image:
                await message.answer_photo(photo=image, caption=f"Картинка {title}")
        else:
            await message.answer(f"Изображение для {title} не найдено.")

    # отправляем инлайн меню
    await message.answer("Выберите продукт для покупки:", reply_markup=get_inline_menu())

# handler на текст "Купить"
@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def handle_buy_command(message: types.Message):
    await get_buying_list(message)

# handler на нажатие кнопки "product_buying"
@dp.callback_query_handler(Text(equals="product_buying"))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

# Функция для кнопки рассчитать
@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

# Функция для кнопки Формула Расчета
@dp.callback_query_handler(lambda call: call.data == "formulas")
async def get_formulas(call: CallbackQuery):
    formula_text = (
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст - 161\n\n"
        "Формула для мужчин:\n"
        "BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5"
    )
    await call.message.answer(formula_text)
    await call.answer()

# Формула для начала машины состояний
@dp.callback_query_handler(lambda call: call.data == "calories")
async def set_age(call: CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()

# Формула для ввода роста
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()

# Формула для ввоба веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

# Формула для расчета калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(data["weight"])

    # Формула для женщин
    bmr = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий составляет примерно {bmr:.2f} ккал.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

