import gspread, time
import numpy as np

sa = gspread.service_account('_Key_.json') #подключение в  json файлу библиотеки
sh = sa.open("Vote_data")  #открытие таблицы с таким-то названием

available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
available_answers = ["за", "против", "воздержусь"]
token="6600311339:AAEtH4iXyC0x005c-lc_EDYKyEarRl9Cdms"
key='00000'

def on_hold(sec: int): time.sleep(sec) # функция задержки 

def check(user_id: str,department_id: int):
    try:
        if sh.get_worksheet(department_id+3).find(user_id) is None: return True
        else: return False
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_candidats()

def get_candidats():
    try:
        sheet3 = sh.get_worksheet(2)  # выбирам третий по порядку лист
        candidats_ATP = sheet3.row_values(1)  # выбирам ПЕРВУЮ строку
        candidats_IVT = sheet3.row_values(2)  # выбирам ВТОРАЯ строку
        candidats_IS = sheet3.row_values(3)  # выбирам ТРЕТЬЯ строку
        candidats_IST = sheet3.row_values(4)  # выбирам ЧЕТВЕРТАЯ строку
        candidats_Pr = sheet3.row_values(5)  # выбирам ПЯТАЯ строку
        return [candidats_ATP,candidats_IVT,candidats_IS,candidats_IST,candidats_Pr] #вывод общего списка кандидатов
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_candidats()

def get_cand():
    try:
        return np.array(sh.get_worksheet(2).get_all_values())
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_cand()


print(f'1:{get_candidats()}\n2:{get_cand()}')


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
        department_worksheet=sh.get_worksheet(department_id+3) #определение рабочей страницы в таблице   
        for itr in range(2,26,1): #перебор столбцов
            votes=department_worksheet.col_values(itr) #определение 
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

def clear_sheets(department_id: int): #очищает клетки в диапозоне
    try: 
        department_worksheet=sh.get_worksheet(department_id+3) #определение рабочей страницы в таблице
        department_worksheet.batch_clear(["A3:Z100"]) #определяем область очистки
    except gspread.exceptions.APIError: 
        on_hold(5)
        return clear_sheets(department_id)
