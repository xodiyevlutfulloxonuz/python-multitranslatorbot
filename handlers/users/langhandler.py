from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command 
from loader import dp
from states.lang import Lang 
from keyboards.inline.langkeyboard import languages
from deep_translator import GoogleTranslator

@dp.callback_query_handler(state=Lang.first_lang)
async def first_lang_function(call:types.CallbackQuery,state=FSMContext):
    await call.message.answer("Tarjima tilini kiriting:",reply_markup=languages)
    await state.update_data({
        "first_lang":call.data 
    })
    await call.message.delete()
    datas=await state.get_data()
    await Lang.next()


@dp.callback_query_handler(state=Lang.second_lang)
async def second_lang_function(call:types.CallbackQuery,state=FSMContext):
    await state.update_data({
        "second_lang":call.data 
    })
    await call.message.delete()
    await call.message.answer("Text kiriting:")
    await Lang.next()


@dp.message_handler(state=Lang.your_text)
async def your_text_function(message:types.Message, state=FSMContext):
     datas= await state.get_data()
     if datas.get('first_lang')!=datas.get('second_lang'):

         await state.update_data({
         "your_text": message.text
         })

         if message.text!="/start":
              datas= await state.get_data()
              translated = GoogleTranslator(source=datas.get('first_lang'), target=datas.get('second_lang')).translate(datas.get('your_text'))
              await message.answer(translated)

         if message.text=="/start":
             await state.finish()
             await message.answer(f" Assalomu alaykum{message.from_user.first_name} botimizga xush kelibsiz.\n"
                         f"<b>Tilni tanlang.</b>",reply_markup=languages)
             await Lang.first_lang.set()

     else:
         await message.answer(f"Kiritilgan va Tarjima qilinadigan til bir xil\n"
                              f"bo'lishi mumkin emas. Qaytadan tanlang.",reply_markup=languages)  
         await Lang.second_lang.set()

        
           

     

    




    

    

    
    
    




    
    
    
    




    


    






