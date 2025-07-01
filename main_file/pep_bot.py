import asyncio
from pyexpat.errors import messages

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command



disp_pep_bot = Bot(token='7700816861:AAGsG8sSbVRjpTQ7Cqriczd7w5PnIbVpE6I')
dp = Dispatcher()



@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Здравствуйте!")
    await message.reply("На связи бот компании 'Петроэнергопроект'! Чем могу Вам помочь?")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Вы нажали на кнопку помощи")


async def main():
    await dp.start_polling(disp_pep_bot)



if __name__=="__main__":
    asyncio.run(main())



