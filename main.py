import asyncio
import logging
import sys
from app.commands.commands import set_my_commands
from aiogram import Bot, Dispatcher, F
from config import TOKEN
from app.handlers.handlers import router
from app.spam_messages.advertising import start_reg, reg_photo, reg_caption
from aiogram.filters import Command
from app.spam_messages.advertising import RegisterState
dp = Dispatcher()
async def main() -> None:
    dp.message.register(start_reg, Command('set_advertise'))
    dp.message.register(reg_photo, RegisterState.reg_photo, F.photo)
    dp.message.register(reg_caption, RegisterState.reg_caption)
    dp.include_router(router=router)
    bot = Bot(TOKEN)
    await set_my_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())