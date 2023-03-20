import pandas as pd
import numpy as np
from data_call import data_call

dict = {'ФИО':["Трифонов Е.А.", "Горский И.А.", "Трифонов Е.А.", "Гросул А.В."],

        'Товар': ["Телефон Iphone 11 pro max", "Телевизор Samsung PlasaTV 55* ", "Наушники AirPods pro max", "Кофемашинка Bosh 1732p"],
        
        'Ссылка на магазин': ["www.mvideo.ru", "www.enter.ru", "www.insales.ru", "www.ozon.ru"],

        'Контакты':["89777737304", "gosky.ilya@gmail.com", "trifon799@gmail.com", "89151597812]"]}

dff = pd.DataFrame(dict)

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame

# Клас add_by расширен  из класса data_call
class add_by(data_call):
    'удаляем магазин по введеному имени'
    def __init__ (self,link_app,id_sites,FIO,tovar):

        # Вызывается constructor родительского класса (data_call)
        # чтобы прикрепить значение к атрибуту 'link_app' родительского класса
        super().__init__(link_app)
        self.id_sites = id_sites
        self.FIO = FIO
        self.tovar = tovar
        
    # Переопределить (override) метод с одинаковым названием родительского класса.
    def by_pisition (self):
        sort_data = data.query("ID == @self.id_sites and LInk == @self.link_app")
        print("вы покупаете у данного магазина")
        print (sort_data)
        print("")
        segment = int (self.id_sites)
        contact_bd = data.loc[data['ID'] == segment, 'Contact'].item() 
        LInk_bd = data.loc[data['ID'] == segment, 'LInk'].item()
        count_row = dff.shape[0] + 1 # весь список и добавляем в конец
        print("Будет добавлен пользователь",self.FIO,",который хочет купить",self.tovar,",у магазина ",LInk_bd,". Контакты магазина ",contact_bd)
        print("")
        dff.loc[count_row] = [self.FIO, self.tovar, LInk_bd, contact_bd]
        print (dff)
        print("")

        
