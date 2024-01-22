from aiogram.types import Message, CallbackQuery
from aiogram import Router
from aiogram.filters import CommandStart
from app.callback.callback_button import MyCallback
from app.keyboards.inline_keyboard import keyboard1
from aiogram import F
router = Router()


@router.callback_query(MyCallback.filter(F.foo == 'allow'))
async def yay(query: CallbackQuery):
    await query.message.answer('будешь заспамлен')


@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer('этот бот будет спамить вам надоедливую рекламу', reply_markup=await keyboard1())