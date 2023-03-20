import pandas as pd
import numpy as np

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame

from data_call import data_call

# Клас data_dell расширен  из класса data_call.
class data_dell(data_call):
    'удаляем магазин по введеному имени'
    
    def __init__ (self,link_app,id_sites):

        # Вызывается constructor родительского класса (data_call)
        # чтобы прикрепить значение к атрибуту 'link_app' родительского класса
        super().__init__(link_app)
        self.id_sites = id_sites

    # Переопределить (override) метод с одинаковым названием родительского класса.
    def deleted_data (self):
        sort_data = data.query("ID == @self.id_sites and LInk == @self.link_app")
        print("будет удалена строка: ")
        print (sort_data)
        #data = data.drop(np.where(data['ID'] == self.id_sites )[0])
        print("data")
            


