from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.callback.callback_button import MyCallback

async def keyboard1():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="разрешить спам",
        callback_data=MyCallback(foo="allow")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    return builder.as_markup()

