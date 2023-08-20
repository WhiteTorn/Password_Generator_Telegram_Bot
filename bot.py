import logging

from aiogram import Bot, Dispatcher, executor, types

import config
import PassGen as ps


"""

Randomize Letters In words (HOW? IDK I WILL DO SOMETHING)

"""

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher

bot = Bot(token=config.TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.message):

    await message.reply("Hello, User \n ° This Bot Will Generate Password and you are free to use them \n But You "
                        "Should Be concerned about using them, \nDO NOT TRUST TELEGRAM\nit means that just do "
                        "not copy generated 'passwords', modify them!!! and save only on PAPER\n /help for commands")


@dp.message_handler(commands=['help'])
async def help_user(message: types.message):

    await message.reply("/weak ——— Generate Small Password (not recommended) \n"
                        "/normal ——— Generate Medium Password (50/50) \n"
                        "/strong ——— Recommended only if you modify it")


@dp.message_handler(commands=['weak'])
async def weak_password(message: types.message):

    await message.answer(ps.weak())


@dp.message_handler(commands=['normal'])
async def weak_password(message: types.message):

    await message.answer(ps.normal())


@dp.message_handler(commands=['strong'])
async def weak_password(message: types.message):

    await message.answer(ps.strong())


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)