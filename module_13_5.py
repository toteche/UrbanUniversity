from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


button_calculate = KeyboardButton(text = 'Рассчитать')
button_info = KeyboardButton(text = 'Информация')
kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_calculate, button_info)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('информация о боте!')

@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data["age"])
    growth = int(data["growth"])
    weight = int(data["weight"])
    calories_norm = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий составляет примерно {calories_norm:.2f} ккал.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
