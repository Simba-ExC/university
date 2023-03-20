from data_call import data_call
from data_dell import data_dell
from data_add import data_add
from all_db import get_bd
from add_by import add_by
import re

def check_phone(num: str):
    clear_phone = re.sub(r'\D', '', num)
    result = re.match(r'^[78]?\d{10}$', clear_phone)
    if bool(result) == 'true':
        return "phone"
    else :
        text = phones_str
        pattern = r"sidorov@([\w\.-]+)(\.[\w\.]+)"
        if re.search(pattern, text):
            return "email"
        else :
            return "unknown" 



print("")
print("по команде “se” осуществим поиск в базе")
print("по команде “ad” добавим магазин в базу")
print("по команде “de” удалим магазин из базы")
print("по команде “all” посмотрим всю Базу данных ")
print("по команде “by” сделаем заказ ")
print("по команде “end” программа закроется ")
print("")
end_str = 'go'
while end_str == 'go':
    txt = input("Веедите команду : ")

    if txt == "se":
        print("")
        print("осущуствим поиск в базе")
        print("")
        link_app = input ("введите ссылку на магазин для поиска: " )
        data_c = data_call(link_app)
        data_c.search_data()

   
    elif txt == "ad":
        print("")
        print("добавим магазин в базу")
        print("")
        link_app = input ("название магазина для добавления: " ) 
        phones_str = input ("введите контакты новoго магазина: " )
        Contact_app = phones_str
        phones = re.split(r' *; *', phones_str, flags=re.M)
        for phone in phones:
            tupe_app = check_phone(phone)
        data_a = data_add(link_app,Contact_app,tupe_app)

        #полиморфизм
        def intro(BD):               
            BD.greeting()
        intro(data_a)
        
    elif txt == "de":
        print("")
        print("удалим магазин из базы")
        print("")
        link_app = input ("введите ссылку на магазин для удаления: " )
        print("")
        data_c = data_call(link_app)
        data_c.search_data()
        id_sites = input ("Выберите ID для удаления : " )
        data_d = data_dell(link_app,id_sites)
        data_d.deleted_data()

    elif txt == "all":

        #полиморфизм
        def intro(BD):               
            BD.greeting()
        flora = get_bd()
        intro(flora)


    elif txt == "by":
        print("")
        print("добавим запрос на покупку представителю магазина")
        print("")
        FIO = input ("Введите ФИО: ")
        tovar = input (" Что вы хотите купить: ")
        link_app = input ("У какого магазина вы хотите заказать товар: " )
        data_c = data_call(link_app)
        data_c.search_data()
        print("")
        id_sites = input ("Выберите ID магазина для покупки у данного магазина: " )

        data_a = add_by(link_app,id_sites,FIO,tovar)
        data_a.by_pisition()
        
    elif txt == "end":
        end_str = 'end'
    else :
        print("Вы ввели", txt , 'такого пункта нету, попробуйте еще раз')
        print("")



