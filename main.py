from aiogram import Bot, Dispatcher, types, executor

from keyboards.inline_keyboard import *
from keyboards.not_inline_keyboards import keyboard, keyboard_1

from config import TOKEN

import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд
/start - запуск бота
/description - описание
/kittens - котики
"""

list_of_photos_urls = ['https://avatars.mds.yandex.net/i?id=0008cc4f75451224109bc851ed46e6968dc35f3a-9044992-images-thumbs&n=13',
                       'https://avatars.mds.yandex.net/i?id=7722d26fb40964f6b402a3d4e0e43f8cd0194863-8972142-images-thumbs&n=13',
                       'https://avatars.mds.yandex.net/i?id=02e3e552a82968de8bc500e5b20962e346498a7c-8981816-images-thumbs&n=13',
                       'https://avatars.mds.yandex.net/i?id=c5cd4a330988d5783f67e52b5c9125505735b11a-7111467-images-thumbs&n=13']

async def on_startup(_):
    print('Бот успешно запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Добро пожаловать!',
                         reply_markup=keyboard)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['description'])
async def desc_command(message: types.Message):
    await message.answer(text='В этом боте ты можешь оценить котиков!')

@dp.message_handler(commands=['kittens'])
async def select_photo(message: types.Message):
    await message.answer(text='Выбери котика!',
                         reply_markup=keyboard_1)

@dp.message_handler(commands=['cat'])
async def cat(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                   photo=random.choice(list_of_photos_urls),
                   caption='Как тебе этот котик?',
                   reply_markup=inlkb)


@dp.message_handler(commands=['home'])
async def home_menu(message: types.Message):
    await message.answer(text='Вы вернулись в главное меню',
                         reply_markup=keyboard)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text='Тебе понравился котик :)')
    elif callback.data == 'next_cat':
        await cat(callback.message)
    else:
        await callback.answer(text='Тебе не понравился котик :(')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)