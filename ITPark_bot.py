import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile

from bot_buttons import cansel_btn, menu, add_btn, jinsi_menu
from new_itpark_bot_class import New_itpark_bot_helperDB
from config import example_bot_token

logging.basicConfig(level=logging.INFO)
bot = Bot(example_bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

base = New_itpark_bot_helperDB("ITPark.db")


class FSMAdmin(StatesGroup):
    fullname = State()
    phoneNumber = State()
    course = State()
    birthday = State()
    jinsi = State()
    passport = State()
    saveData = State()


async def start_command(message: types.Message):
    print(message.from_user.username)
    await message.reply(f'Assalomu aleykum {message.from_user.username}'
                        f' ITParkning rasmiy botiga hush kelibsiz')
    await message.answer("IT kurslarda o'qishni boshlaganingizdan xursandmiz."
                         "sizni talaba sifatida ro‘yxatdan o‘tkazishimiz uchun,"
                         "siz o'z ma’lumotlaringizni to‘g‘ri to‘ldirishingiz lozim.\n"
                         "\n"
                         "Qani kettik!")
    await FSMAdmin.fullname.set()
    await message.answer("Familya va Ism (pasport/metrikada ko'rsatilganidek)", reply_markup=cansel_btn)


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
        await message.answer("Tug'ilgan sana (masalan 31.12.2000)", reply_markup=cansel_btn)

async def get_birthday(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(birthday=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Jinsingizni tanlang👇👇", reply_markup=jinsi_menu)

async def get_jinsi(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(jinsi=message.text.strip())
        await FSMAdmin.next()
        await message.bot.send_photo(chat_id=message.from_user.id,
                                     photo=InputFile("D:\IT dars\photo_2023-11-23_18-19-18.jpg"))
        await message.reply("Face ID uchun o'z rasmingizni yuklang", reply_markup=cansel_btn)


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

async def get_users(message: types.Message):
    for i in base.select_item():
        await message.answer(f"Barcha userlar ro'yxati {i}")
        print("Userlar ro'yxati chiqarildi!!")

async def register(message: types.Message, state: FSMContext):
    print('################################')
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        async with state.proxy() as data:
            print(data["fullname"], data["phoneNumber"], data["course"])
            base.add_item(data["fullname"], data["phoneNumber"], data["course"],
                          data['birthday'], data['jinsi'], data["passport"])
        await state.finish()
        await message.answer("Malumotlar muvaffaqiyatli saqlandi")
        await message.answer("Yangi talaba qo'shish uchun /start deb yozing")


def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(start_command, commands=['start'], state=None)  # start
    dp1.register_message_handler(get_fullname, state=FSMAdmin.fullname)  # fullname
    dp1.register_message_handler(get_PhoneNumber, state=FSMAdmin.phoneNumber)  # tel
    dp1.register_message_handler(get_course, state=FSMAdmin.course)  # course
    dp1.register_message_handler(get_birthday, state=FSMAdmin.birthday)  # birthday
    dp1.register_message_handler(get_jinsi, state=FSMAdmin.jinsi)  # jinsi
    dp1.register_message_handler(get_photo, state=FSMAdmin.passport, content_types="photo")  # photo
    dp1.register_message_handler(get_users, commands=["get_users"], state=None)
    dp1.register_message_handler(register, state=FSMAdmin.saveData)  # save data

async def on_startup(dp: Dispatcher):
    base.create_table('Students')
    print('Bot ishga tushdi ')

async def on_shutdown(dp: Dispatcher):
    print("Good bye!")
    base.log_out()

if __name__ == "__main__":
    register_handler_admin(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)

