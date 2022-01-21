import logging
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler 
from utils.misc import subscription 
from loader import bot 
from data.config import CHANNELS 

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update:types.Update, data:dict):
        if update.message:
            user=update.message.from_user.id
        
        elif update.callback_query:
            user=update.callback_query.from_user.id
        
        else: return
        logging.info(user)

        result="Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling.\n "
        final_status=True 
        for channel in CHANNELS:
            status=await subscription.check(user_id=user, channel=channel)
            final_status*=status 
            channel=await bot.get_chat(channel)
            if not status:
                invite_link=await channel.export_invite_link()
                result+=(f"✅ <a href='{invite_link}'>{channel.title}</a>\n")
        
        result+="Obuna bo'lgandan so'ng qaytadan /start buyrug'ini ustiga bosing"
        result=f"<b>{result}</b>"

        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True)
            raise CancelHandler()