from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5229403861:AAFdxFe9nFrv_cBsibOyxHKZZwgIeQWBhmU'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    await msg.answer("Привет! Меня зовут Поздравлятор. \nЕсли хочешь ознакомиться с тем, что я умею - напиши /help")

@dp.message_handler(commands=['help'])
async def help_message(msg: types.Message):
    await msg.answer('Ну вот ты и прописал /help')

@dp.message_handler()
async def echo(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Извини, я не знаю как на это ответить')

if __name__ == '__main__':
    executor.start_polling(dp)