from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton#, ReplyKeyboardRemove

# b1 = KeyboardButton('/Режим_работы')
# b2 = KeyboardButton('/Расположение')
# b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)
buttons = ["Адрес", "Режим работы", "Товары"]

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)#, one_time_keyboard=True)
# kb_client.add(b1).add(b2).insert(b3).row(b4, b5)
# kb_client.insert(b1).insert(b2).insert(b3) # .row(b4, b5)

kb_client_start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)#, one_time_keyboard=True)
kb_client_start.add(*buttons)

inl_kb_btns = ["1", "2", "3"]
inl_kb_btn_1 = InlineKeyboardButton('1', callback_data='button1')
inl_kb_btn_2 = InlineKeyboardButton('2', callback_data='button2')
inl_kb_btn_3 = InlineKeyboardButton('3', callback_data='button3')

kb_client_categories = InlineKeyboardMarkup().add(inl_kb_btn_1, inl_kb_btn_2, inl_kb_btn_3)

