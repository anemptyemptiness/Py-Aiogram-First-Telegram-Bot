from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
kb_btn_1 = KeyboardButton('/start')
kb_btn_2 = KeyboardButton('/help')
kb_btn_3 = KeyboardButton('/description')
kb_btn_4 = KeyboardButton('/kittens')

keyboard.add(kb_btn_1).add(kb_btn_2).add(kb_btn_3).add(kb_btn_4)

keyboard_1 = ReplyKeyboardMarkup(resize_keyboard=True)
k1_btn_1 = KeyboardButton('/cat')
k1_btn_4 = KeyboardButton('/home')

keyboard_1.add(k1_btn_1).add(k1_btn_4)