import logging

from aiogram import Bot,Dispatcher,executor,types

from checkWord import checkWords

API_TOKEN = '5511967797:AAFYPsQlD3dz3TiKD7xfoZwamCVcZ3jXfaQ'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async  def send_welcome(message:types.Message):
    await message.reply("Uz imlo botiga hush kelibsiz!")

@dp.message_handler(commands='help')
async def help_user(message :types.Message):
    await message.reply("Bo'tdan foydalash uchun so'z yuboring!!!")

@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWords(word)
    if result['available']:
        response = f"To'g'ri: {word.capitalize()}"
    else:
        response = f"Noto'g'ri: {word.capitalize()}\n"
        for text in result['matches']:
            response += f"{text.capitalize()}\n"

    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
