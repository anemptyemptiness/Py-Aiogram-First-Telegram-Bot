from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inlkb = InlineKeyboardMarkup(row_width=2)
inlbtn_1 = InlineKeyboardButton(text='Нравится!!',
                                callback_data='like')
inlbtn_2 = InlineKeyboardButton(text='Не нравится((',
                                callback_data='dislike')
inlbtn_3 = InlineKeyboardButton(text='Следующий котик',
                                callback_data='next_cat')

inlkb.add(inlbtn_1).insert(inlbtn_2).add(inlbtn_3)

