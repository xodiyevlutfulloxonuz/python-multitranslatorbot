from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton 
languages=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='uz', callback_data='uz'), 
        InlineKeyboardButton(text='en', callback_data='en')
        ],
         [
        InlineKeyboardButton(text='ru', callback_data='ru'), 
        InlineKeyboardButton(text='arab', callback_data='ar')
        ],

    ]
)

change_lang=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="boshqa qaytish", callback_data="bosh")]
    ]
)
