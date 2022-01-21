from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.subscription import check_btn 
from keyboards.inline.langkeyboard import languages
from loader import dp, bot                   
from utils.misc import subscription 
from states.lang import Lang 
from data.config import CHANNELS





@dp.message_handler(CommandStart())
async def show_channels(message: types.Message, state="*"):
    await message.answer(f" Assalomu alaykum <b> {message.from_user.first_name} </b> botimizga xush kelibsiz.\n"
                         f"<b>Tilni tanlang.</b>",reply_markup=languages)
    await Lang.first_lang.set()

    
   














