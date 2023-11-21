from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn1 = KeyboardButton('Backend')
btn2 = KeyboardButton('Frontend')
btn3 = KeyboardButton('Mobil dasturlash')
btn4 = KeyboardButton('Robototehnika')
btn5 = KeyboardButton('UI/UX')
btn6 = KeyboardButton('Foundation')
cansel = KeyboardButton('So`rovni tugatish!')

yangi_talaba = KeyboardButton("Talaba qo'shish")

saveBTN = KeyboardButton('Saqlash')

menu = (ReplyKeyboardMarkup(resize_keyboard=True)
        .add(btn1, btn2).add(btn3).add(btn4, btn5).add(btn6).add(cansel))

cansel_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(cansel)

add_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(saveBTN, cansel)

new_user = ReplyKeyboardMarkup(resize_keyboard=True).add(yangi_talaba)

