import gspread, time
import numpy as np

sa = gspread.service_account('_Key_.json') #подключение в  json файлу библиотеки
sh = sa.open("Vote_data")  #открытие таблицы с таким-то названием

available_departmemts= ["АТП", "ИВТ", "ИБ", "ИСТ", "Приборостроение"]
available_answers = ["за", "против", "воздержусь"]
token="6600311339:AAEtH4iXyC0x005c-lc_EDYKyEarRl9Cdms"
key='00000'

def on_hold(sec: int): time.sleep(sec) # функция задержки 

def check(user_id: str,dp_id: int): #проверка на наличие id пользователя в системе
    try:
        if sh.get_worksheet(dp_id+3).find(user_id) is None: return True
        else: return False
    except gspread.exceptions.APIError:
        on_hold(5)
        return check(user_id,dp_id)

def get_contenders():
    try:
        list_=sh.get_worksheet(2).get_all_values() # список всех элементов страницы с кандидатами
        return [[x for x in item if x] for item in list_]
    except gspread.exceptions.APIError:
        on_hold(5)
        return get_contenders()

def pass_user_data(user_id: str,dp_id: int,myList: list): #принимаем id пользователя и список ответов
    try:
        worksheet=sh.get_worksheet(dp_id+3) #определение рабочей страницы в таблице
        last_row = len(worksheet.get_values()) + 1 #получение последнего значения заполненной строки +1 
        if check(user_id,  dp_id) is True: #проверям на наличие id в таблице
            myList.insert(0,user_id) # Добавляем id на первое место в списке
            for col in range(1, len(myList)+1,1): #заполнение через for(1, длинна списка ответов, шаг 1)
                worksheet.update_cell(last_row, col, myList[col-1]) #определяем место ввода(поселдняя свободная, столбец, значение)
        else: return False 
    except gspread.exceptions.APIError:
        on_hold(5)
        return pass_user_data(user_id,dp_id,myList)
    
def get_results(dp_id: int) -> list: #результаты голосования
    try:
        list_=np.array(sh.get_worksheet(dp_id+3).get_values()).T[1:] #список кандидатов и результаты
        result_list=np.array([[item[0],np.count_nonzero(item=='за')] for item in list_]) #список кандидатов и голоса за
        max_index = np.argmax(result_list[:, 1]) #индекс списка с максимальным числом голосов
        return result_list[max_index] #вывод списка по индексу
    except gspread.exceptions.APIError: 
        on_hold(5)
        return get_results(dp_id)
    
print(get_results(1))

def clear_sheets(dp_id: int): #очищает клетки в диапозоне
    try: 
        sh.get_worksheet(dp_id+3).batch_clear(["A3:Z100"]) #определяем область очистки
    except gspread.exceptions.APIError: 
        on_hold(5)
        return clear_sheets(dp_id)
