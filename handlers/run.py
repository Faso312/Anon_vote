from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types, html
from .DB import pass_user_data, get_candidats, check
from keyboards.dinemic_kb import make_row_keyboard

available_answers = ["за", "против", "воздержусь"]
available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
reply_after_quiz=["Спасибо вам за участие в секретном голосовании! Ваш голос имеет большое значение и помогает нам принимать важные решения. Мы ценим ваше мнение и благодарим вас за вклад в нашу работу!"]
local_cand_list=get_candidats()

router = Router()


class Answer_class(StatesGroup): 
    choose_department=State()
    check=State()
    ans_q1 = State()
    ans_q2 = State()
    ans_q3 = State()
    ans_q4 = State()
    ans_q5 = State()
    ans_q6 = State()
    ans_q7 = State()
    ans_q8 = State()
    ans_q9 = State()
    ans_q10 = State()
    ans_q11 = State()
    ans_q12 = State()
    ans_q13 = State()
    ans_q14 = State()
    ans_q15 = State()
    ans_q16 = State()
    ans_q17 = State()
    ans_q18 = State()
    ans_q19 = State()
    ans_q20 = State()
    ans_q21 = State()
    ans_q22 = State()
    ans_q23 = State()
    ans_q24 = State()
    ans_q25 = State()
    

def update_cand_list(): #функция обновления списка кандидатов
    global local_cand_list
    local_cand_list=get_candidats()
    
@router.callback_query(F.data == 'to_vote')
async def running(callback: types.CallbackQuery, state: FSMContext): 
    await state.clear()  
    await callback.message.answer(f'Выберите кафедру',reply_markup=make_row_keyboard(available_departmemts))
    await state.set_state(Answer_class.choose_department) #Устанавливаем пользователю состояние "выбирает ответ"
    await callback.answer()


@router.message(Answer_class.choose_department, F.text.in_(available_departmemts))
async def answering_q1(message: Message, state: FSMContext):  #задание 1 вопроса
    await state.update_data(department=message.text)
    user_data = await state.get_data()
    if check(str(message.from_user.id), int(available_departmemts.index(user_data['department']))) is True:
        await message.answer(
            str(local_cand_list[int(available_departmemts.index(user_data['department']))][0]),
            reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q1)
    else: 
        await message.answer(f'Вы уже голосовали',reply_markup=ReplyKeyboardRemove())
        await state.clear()


@router.message(Answer_class.ans_q1, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 2 вопроса
    await state.update_data(ans1=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][1]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q2)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q2, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 3 вопроса
    await state.update_data(ans2=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][2]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q3)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()
     
        
@router.message(Answer_class.ans_q3, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 4 вопроса
    await state.update_data(ans3=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][3]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q4)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q4, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 5 вопроса
    await state.update_data(ans4=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][4]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q5)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q5, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 6 вопроса
    await state.update_data(ans5=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][5]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q6)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q6, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 7 вопроса
    await state.update_data(ans6=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][6]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q7)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q7, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 8 вопроса
    await state.update_data(ans7=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][7]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q8)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q8, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 9 вопроса
    await state.update_data(ans8=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][8]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q9)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()


@router.message(Answer_class.ans_q9, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 10 вопроса
    await state.update_data(ans9=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][9]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q10)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()
        
        
@router.message(Answer_class.ans_q10, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 11 вопроса
    await state.update_data(ans10=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][10]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q11)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()     
        
   
@router.message(Answer_class.ans_q11, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 12 вопроса
    await state.update_data(ans11=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][11]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q12)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          
        
        
@router.message(Answer_class.ans_q12, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 13 вопроса
    await state.update_data(ans12=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][12]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q13)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          
        
        
@router.message(Answer_class.ans_q13, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 14 вопроса
    await state.update_data(ans13=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][13]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q14)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          
        
        
@router.message(Answer_class.ans_q14, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 15 вопроса
    await state.update_data(ans14=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][14]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q15)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          
        
        
@router.message(Answer_class.ans_q15, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 16 вопроса
    await state.update_data(ans15=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][15]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q16)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          


@router.message(Answer_class.ans_q16, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 17 вопроса
    await state.update_data(ans16=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][16]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q17)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          


@router.message(Answer_class.ans_q17, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 18 вопроса
    await state.update_data(ans17=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][17]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q18)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

        
@router.message(Answer_class.ans_q18, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 19 вопроса
    await state.update_data(ans18=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][18]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q19)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          


@router.message(Answer_class.ans_q19, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 20 вопроса
    await state.update_data(ans19=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][19]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q20)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

        
@router.message(Answer_class.ans_q20, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 21 вопроса
    await state.update_data(ans20=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][20]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q21)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

   
@router.message(Answer_class.ans_q21, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 22 вопроса
    await state.update_data(ans21=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][21]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q22)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

   
@router.message(Answer_class.ans_q22, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 23 вопроса
    await state.update_data(ans22=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][22]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q23)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

   
@router.message(Answer_class.ans_q23, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 24 вопроса
    await state.update_data(ans23=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][23]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q24)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

   
@router.message(Answer_class.ans_q24, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  # задание 25 вопроса
    await state.update_data(ans24=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][24]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q25)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

   
@router.message(Answer_class.ans_q25, F.text.in_(available_answers))
async def answering_q1(message: Message, state: FSMContext):  
    await state.update_data(ans25=message.text.lower())
    user_data = await state.get_data()
    try:
        await message.answer(str(local_cand_list[int(available_departmemts.index(user_data['department']))][25]),reply_markup=make_row_keyboard(available_answers))
        await state.set_state(Answer_class.ans_q26)
    except IndexError:
        await message.answer(text=f"{reply_after_quiz[0]}",reply_markup=ReplyKeyboardRemove())
        list_=list(user_data.values())[1:] #Сброс состояния и сохранённых данных у пользователя
        pass_user_data(str(message.from_user.id),int(available_departmemts.index(user_data['department'])),list_ )
        await state.clear()          

@router.message(Answer_class.ans_q1)
@router.message(Answer_class.ans_q2)
@router.message(Answer_class.ans_q3)
@router.message(Answer_class.ans_q4)
@router.message(Answer_class.ans_q5)
@router.message(Answer_class.ans_q6)
@router.message(Answer_class.ans_q7)
@router.message(Answer_class.ans_q8)
@router.message(Answer_class.ans_q9)
@router.message(Answer_class.ans_q10)
@router.message(Answer_class.ans_q11)
@router.message(Answer_class.ans_q12)
@router.message(Answer_class.ans_q13)
@router.message(Answer_class.ans_q14)
@router.message(Answer_class.ans_q15)
@router.message(Answer_class.ans_q16)
@router.message(Answer_class.ans_q17)
@router.message(Answer_class.ans_q18)
@router.message(Answer_class.ans_q19)
@router.message(Answer_class.ans_q20)
@router.message(Answer_class.ans_q21)
@router.message(Answer_class.ans_q22)
@router.message(Answer_class.ans_q23)
@router.message(Answer_class.ans_q24)
@router.message(Answer_class.ans_q25)
async def wrong_answer1(message: Message):  #проверка ответов
    await message.answer(f"Отвечайте {html.underline(html.quote(available_answers[0]))} , {html.underline(html.quote(available_answers[1]))} или {html.underline(html.quote(available_answers[2]))}\nДля удобства восползуйтесь клавиатурой ниже", parse_mode="HTML",
        reply_markup=make_row_keyboard(available_answers))
