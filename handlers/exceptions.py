from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def answer_on_text(message: Message):
    await message.answer(text=f'Обратитесь к /help.')
