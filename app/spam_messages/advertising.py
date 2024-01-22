from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram import Router
from aiogram import Bot
router_advertise = Router()


class RegisterState(StatesGroup):
    reg_photo: str = State()
    reg_caption: str = State()


async def start_reg(message: Message, state: FSMContext):
    await state.set_state(RegisterState.reg_photo)
    await message.answer('отправь фото своей рекламы')


async def reg_photo(message: Message, state: FSMContext):
    await message.answer('окей теперь пришли подпись под фото')
    await state.set_state(RegisterState.reg_caption)
    await state.update_data(reg_photo=message.photo[-1].file_id)


async def reg_caption(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(reg_caption=message.text)
    await message.answer('все готово теперь реклама будет переслана всем пользователям')
    reg_data = await state.get_data()

    reg_photo = reg_data.get('reg_photo')
    reg_caption = reg_data.get('reg_caption')

    await bot.send_photo(chat_id=message.from_user.id, photo=reg_photo, caption=reg_caption)