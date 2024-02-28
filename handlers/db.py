import gspread, time
import numpy as np

sa = gspread.service_account('_Key_.json') #подключение в  json файлу библиотеки
sh = sa.open("Vote_data")  #открытие таблицы с таким-то названием

available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
available_answers = ["за", "против", "воздержусь"]
token="6600311339:AAEtH4iXyC0x005c-lc_EDYKyEarRl9Cdms"
key='00000'

def on_hold(sec: int): time.sleep(sec) # функция задержки 

def check(user_id: str,department_id: int): #проверка на наличие id пользователя в системе
    try:
        if sh.get_worksheet(department_id+3).find(user_id) is None: return True
        else: return False
    except gspread.exceptions.APIError:
        on_hold(5)
        return check(user_id,department_id)

def get_contenders():
    try:
        list_=sh.get_worksheet(2).get_all_values() # список всех элементов страницы с кандидатами
        return [[x for x in item if x] for item in list_]
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_contenders()

def pass_user_data(user_id: str,department_id: int,myList: list): #принимаем id пользователя и список ответов
    try:
        worksheet=sh.get_worksheet(department_id+3) #определение рабочей страницы в таблице
        last_row = len(worksheet.get_all_values()) + 1 #получение последнего значения заполненной строки +1 
        if check(user_id,  department_id) is True: #проверям на наличие id в таблице
            myList.insert(0,user_id) # Добавляем id на первое место в списке
            for col in range(1, len(myList)+1,1): #заполнение через for(1, длинна списка ответов, шаг 1)
                worksheet.update_cell(last_row, col, myList[col-1]) #определяем место ввода(поселдняя свободная, столбец, значение)
        else: return False 
    except gspread.exceptions.APIError:
        on_hold(5)
        return pass_user_data(user_id,department_id,myList)

def get_vote_results(department_id: int) -> list: 
    try:
        vote_list=[] #создаем локальный список голосов
        worksheet=sh.get_worksheet(department_id+3) #определение рабочей страницы в таблице   
        for itr in range(2,26,1): #перебор столбцов
            votes=worksheet.col_values(itr) #определение 
            if votes: #bool  проверка на пустые столбцы
                candidate=votes[0] #вопрос(имя кандидата)
                votes_for=votes.count('за') #голоса за 
                vote_list.extend([candidate,votes_for]) #подставление значений в список
        max_Value=max([vote_list[itr] for itr in range(1, len(vote_list),2)]) #получаем маскимальное значения
        winner_value=vote_list[int(vote_list.index(max_Value))-1] #получаем имя победителя
        return [winner_value,max_Value] #возвращаем список(имя-за)
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_vote_results(department_id)
    
def get_results(dp_id: int) -> list[list]: 
    t=sh.get_worksheet(dp_id+3)
    print(t)
    worksheet=np.array(t).T #определение рабочей страницы в таблице   
    print(worksheet)
get_results(1)
def clear_sheets(department_id: int): #очищает клетки в диапозоне
    try: 
        sh.get_worksheet(department_id+3).batch_clear(["A3:Z100"]) #определяем область очистки
    except gspread.exceptions.APIError: 
        on_hold(5)
        return clear_sheets(department_id)
