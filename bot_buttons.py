from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

in_btn1 = InlineKeyboardButton('Backend', callback_data="Backend")
in_btn2 = InlineKeyboardButton('Frontend', callback_data="Frontend")
in_btn3 = InlineKeyboardButton('Mobil dasturlash', callback_data='Mobil dasturlash')
in_btn4 = InlineKeyboardButton('Robototehnika', callback_data='Robototehnika')
in_btn5 = InlineKeyboardButton('UI/UX', callback_data='UI/UX')
in_btn6 = InlineKeyboardButton('Foundation', callback_data='Foundation')

btn1 = KeyboardButton('Backend', callback_data="Backend")
btn2 = KeyboardButton('Frontend', callback_data="Frontend")
btn3 = KeyboardButton('Mobil dasturlash', callback_data='Mobil dasturlash')
btn4 = KeyboardButton('Robototehnika', callback_data='Robototehnika')
btn5 = KeyboardButton('UI/UX', callback_data='UI/UX')
btn6 = KeyboardButton('Foundation', callback_data='Foundation')
cansel = KeyboardButton('So`rovni tugatish!', callback_data='So`rovni tugatish!')

erk = KeyboardButton("Erkak")
ayol = KeyboardButton("Ayol")

yangi_talaba = KeyboardButton("Talaba qo'shish")

saveBTN = KeyboardButton('Saqlash')

menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2).add(btn3).add(btn4,
                                btn5).add(btn6).add(cansel)

jinsi_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(erk, ayol)

# menu = (InlineKeyboardMarkup(resize_keyboard=True)
#         .add(btn1, btn2).add(btn3).add(btn4, btn5).add(btn6).add(cansel))

cansel_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(cansel)

add_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(saveBTN, cansel)

new_user = ReplyKeyboardMarkup(resize_keyboard=True).add(yangi_talaba)

