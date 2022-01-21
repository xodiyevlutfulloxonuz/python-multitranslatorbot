from aiogram import types
from loader import dp

# Echo bot
@dp.message_handler(state=None)
async def send_wiki(message: types.Message):
    await message.answer(message.text)

