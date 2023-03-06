import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import PassGen as ps


# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.message):

    await message.reply("WILL BE CONFIGURED")

@dp.message_handler(commands=['help'])
async def help_user(message: types.message):

    await message.reply("IN DEVELOPMENT")

@dp.message_handler(commands=['weak'])
async def weak_password(message: types.message):

    await message.answer(ps.weak())


@dp.message_handler(commands=['normal'])
async def weak_password(message: types.message):

    await message.answer(ps.random_capitalisation(ps.normal(), 3/10.0))


@dp.message_handler(commands=['strong'])
async def weak_password(message: types.message):

    await message.answer(ps.random_capitalisation(ps.strong(), 5/10.0))

@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)