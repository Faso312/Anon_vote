from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
from .DB import get_vote_results
from keyboards.dinemic_kb import make_row_keyboard


available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
key='00000'

router = Router()

class navigate(StatesGroup):
    choose_department=State()
    insert_key=State()

@router.callback_query(F.data == 'get_results')
async def running(callback: types.CallbackQuery, state: FSMContext): 
    await state.clear()  
    await callback.message.answer(f'Выберите кафедру',reply_markup=make_row_keyboard(available_departmemts))
    await state.set_state(navigate.choose_department) #Устанавливаем пользователю состояние "выбирает ответ"
    await callback.answer()
    


@router.message(navigate.choose_department, F.text.in_(available_departmemts))
async def setting_departmant(message: Message, state: FSMContext):  #получаем результаты голосования
    await state.update_data(department=message.text)
    await message.answer(f"Введите секретный ключ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(navigate.insert_key)
    
    
@router.message(navigate.insert_key,F.text)
async def try_key(message: Message, state: FSMContext):
    if message.text == key:
        user_data = await state.get_data()   
        results=get_vote_results(int(available_departmemts.index(user_data['department'])))
        await message.answer(f"🎉Поздарвляем, {results[0]} с каферды {user_data['department']}🎉 \nЗа этого кандидата проголосовало {results[1]} человек", reply_markup=ReplyKeyboardRemove())
        await state.clear()  
    else: 
        await message.answer(f'Неверный ключ',reply_markup=make_row_keyboard(available_departmemts))
    