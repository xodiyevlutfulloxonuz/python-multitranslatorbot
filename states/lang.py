from aiogram.dispatcher.filters.state import StatesGroup,State

class Lang(StatesGroup):
    first_lang=State()
    second_lang=State()
    your_text=State()
