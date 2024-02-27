from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
from .db import get_vote_results, clear_sheets
from .run import update_cand_list as update_
from keyboards.dinemic_kb import make_row_keyboard
from keyboards.static_kb import get_admin_kb, get_choice_keyboard


available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
key='00000'

router = Router()

class navigate(StatesGroup):
    insert_key=State()
    choose_department=State()


@router.callback_query(F.data == 'admin')
async def admin_kb(callback: types.CallbackQuery, state: FSMContext): # клавиатура админа
    await state.clear()  
    await callback.message.answer(f"Введите секретный ключ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(navigate.insert_key)

@router.message(navigate.insert_key,F.text)
async def try_key(message: Message, state: FSMContext): # проверка ключа
    if message.text == key:
        await message.answer(f'Функции администратора:', reply_markup=get_admin_kb())
    else: 
        await message.answer(f'Неверный ключ', reply_markup=ReplyKeyboardRemove())

# results_________________________________________
@router.callback_query(F.data == 'get_results')
async def running(callback: types.CallbackQuery, state: FSMContext): 
    try:
        await callback.message.answer(f'Выберите кафедру',reply_markup=make_row_keyboard(available_departmemts))
        await state.set_state(navigate.choose_department) #Устанавливаем пользователю состояние "выбирает ответ"
        await callback.answer() 
    except Exception as e:  await callback.message.answer(f'Ошибка: {e}, Обратитесь к админитстратору')
    

@router.message(navigate.choose_department, F.text.in_(available_departmemts))
async def setting_departmant(message: Message, state: FSMContext):  #получаем результаты голосования
    await state.update_data(department=message.text)
    user_data = await state.get_data()   
    results=get_vote_results(int(available_departmemts.index(user_data['department'])))
    await message.answer(f"🎉Поздарвляем, {results[0]} с каферды {user_data['department']}🎉 \nЗа этого кандидата проголосовало {results[1]} человек", reply_markup=ReplyKeyboardRemove())
    await state.clear() 
# _________________________________________results

# update_________________________________________
@router.callback_query(F.data == 'update')
async def admin_kb(callback: types.CallbackQuery, state: FSMContext): # клавиатура админа
    try:
        update_()
        await callback.message.answer(f"Данные обновлены", reply_markup=ReplyKeyboardRemove())
        await callback.answer() 
        await state.clear()  
    except Exception as e:  await callback.message.answer(f'Ошибка: {e}, Обратитесь к админитстратору')
# _________________________________________update
    
# clear_sheet_________________________________________
@router.callback_query(F.data == 'clear_sheet')
async def admin_kb(callback: types.CallbackQuery, state: FSMContext): # клавиатура админа
    await callback.message.answer(f'Выберите кафедру', reply_markup=make_row_keyboard(available_departmemts))
    await state.set_state(navigate.choose_department) #Устанавливаем пользователю состояние "выбирает ответ"
    await callback.answer() 

@router.message(navigate.choose_department, F.text.in_(available_departmemts))
async def setting_departmant(message: Message, state: FSMContext):  #получаем результаты голосования
    user_data = await state.get_data()   
    clear_sheets(int(available_departmemts.index(user_data['department'])))
    await message.answer(f'Данные обновлены', reply_markup=ReplyKeyboardRemove())
    await state.clear() 
# _________________________________________clear_sheet

    