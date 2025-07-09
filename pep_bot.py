import asyncio
from aiogram import Bot, Dispatcher
from main_file.app.handlers import router


async def main():
    disp_pep_bot = Bot(token='7700816861:AAGsG8sSbVRjpTQ7Cqriczd7w5PnIbVpE6I')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(disp_pep_bot)


if __name__=="__main__":
    asyncio.run(main())



