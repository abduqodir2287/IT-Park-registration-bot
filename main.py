import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove

from IT_park_bot_token import bot_token
from bot_buttons import cansel_btn, menu, add_btn
from itpark_bot_class import Itpark_bot_helperDB

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

base = Itpark_bot_helperDB("ITPark.db")


class FSMAdmin(StatesGroup):
    fullname = State()
    phoneNumber = State()
    course = State()
    passport = State()
    saveData = State()


async def start_command(message: types.Message):
    print(message.from_user.username)
    await message.reply(f'Assalomu aleykum {message.from_user.username}'
                        f' ITParkning rasmiy botiga hush kelibsiz')
    await FSMAdmin.fullname.set()
    await message.answer('To`liq ismingizni kiriting: ', reply_markup=cansel_btn)


async def get_fullname(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(fullname=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Telefon raqamingizni kiriting(+998...): ")


async def get_PhoneNumber(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(phoneNumber=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Qanday yo`nalishda o`qimoqchisiz: ", reply_markup=menu)


async def get_course(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(course=message.text.strip())
        await FSMAdmin.next()
        await message.answer('Passport rasmini jonating:', reply_markup=ReplyKeyboardRemove())


async def get_photo(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        async with state.proxy() as data:
            await message.photo[-1].download(destination_file=f"{data['fullname']}.png", make_dirs=False)
            await state.update_data(passport=message.photo[0].file_id)
            await FSMAdmin.next()
            print('Rasm muvafaqiyatli saqlandi')
        await message.answer("Malumotlar uchun rahmat", reply_markup=add_btn)


async def register(message: types.Message, state: FSMContext):
    print('################################')
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        async with state.proxy() as data:
            print(data["fullname"], data["phoneNumber"], data["course"])
            base.add_item(data["fullname"], data["phoneNumber"], data["course"], data["passport"])
        await state.finish()
        await message.answer("Malumotlar muvaffaqiyatli saqlandi")
        await message.answer("Yangi talaba qo'shish uchun /start deb yozing")
    print('111111111111111111')



def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(start_command, commands=['start'], state=None)  # start
    dp1.register_message_handler(get_fullname, state=FSMAdmin.fullname)  # fullname
    dp1.register_message_handler(get_PhoneNumber, state=FSMAdmin.phoneNumber)  # tel
    dp1.register_message_handler(get_course, state=FSMAdmin.course)  # course
    dp1.register_message_handler(get_photo, state=FSMAdmin.passport, content_types="photo")  # photo
    dp1.register_message_handler(register, state=FSMAdmin.saveData)  # save data

async def on_startup(dp: Dispatcher):
    base.create_table('Student')
    print('Bot ishga tushdi ')

async def on_shutdown(dp: Dispatcher):
    print("Good bye!")
    base.log_out()

if __name__ == "__main__":
    register_handler_admin(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
