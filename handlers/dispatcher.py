from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.static_kb import get_choice_keyboard

greeting = ["! 👋 Я рад приветствовать вас в нашем боте для анонимного голосования! Здесь вы можете высказать свое мнение по различным вопросам, не раскрывая своей личности. Давай начнем голосование прямо сейчас! 🗳️"]

router = Router()

@router.message(Command('start','choice','menu','help'))
async def cmd_start_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Привет, {message.chat.first_name}! {greeting[0]}',reply_markup=get_choice_keyboard())


