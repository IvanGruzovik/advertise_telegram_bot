from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram import Bot
async def set_my_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='начать'
        ),
        BotCommand(
            command='set_advertise',
            description='сделать свою рекламу'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())