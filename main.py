# Code author: Dagaraliyev Asliddinbek.

import logging
from aiogram import Bot, Dispatcher, executor, types
from muslimsalat import prayer_times
from datetimeA import todays_date
API_TOKEN = 'Your bot token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    #print(message)
    await message.reply(f"<b>👋 Assalomu alaykum {message.from_user.first_name}</b>"\
    f"\n☪️ Namoz vaqtlari botiga xush kelibsiz!!!\n\n⏰ Bugungi namoz vaqtlarini olish uchun iltimos menga <i>vaqt</i> so'zini yozib yuboring!"
    f"\n\n⚠️ Eslatma:"
    f"\nKo'rinadigan namoz vaqtlari faqat <i>Namangan</i> vaqtiga amal qiladi...")

@dp.message_handler(commands=['help'])
async def help_me(message: types.Message):
    await message.reply(f"<b>⚠️ Botda muommo yuzaga kelgan bo'lsa, bot admini bilan bog'laning!</b>"
                        f"\n\n👨‍💻 https://t.me/Asliddinbek_official")

@dp.message_handler()
async def times(message: types.Message):
    times = prayer_times()
    p_times = ""
    today = todays_date()
    today = str(today)
    p_times += f"🗓 <b>Bugungi sana: {today}</b>\n"

    for p, t in times.items():
        time = f"<b>{p}</b>: {t}"
        p_times += f"\n{time}"
    await message.answer(p_times)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)