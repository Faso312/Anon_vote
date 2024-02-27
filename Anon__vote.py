import asyncio, logging
from aiogram import Bot, Dispatcher
from handlers import admin, dispatcher, exceptions, run
from handlers.db import token


logging.basicConfig(level=logging.INFO)

# Настройка бота
bot = Bot(token)
dp = Dispatcher()


async def main():
    dp.include_router(dispatcher.router)
    dp.include_router(run.router)
    dp.include_router(admin.router)
    dp.include_router(exceptions.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

try:
    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt: print(f'Работа приостановлена.....')
except Exception as e: print(f'ошибка вида: {e}')

