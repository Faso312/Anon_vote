from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_choice_keyboard():
    buttons = InlineKeyboardBuilder()
    buttons.button(text='Пройти голосования', callback_data='to_vote')
    buttons.button(text='Результаты голосования', callback_data='get_results')
    buttons.adjust(1)
    return buttons.as_markup()



    

