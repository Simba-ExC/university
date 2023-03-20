import pandas as pd
import numpy as np

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame


class data_call:
    'ищем магазин по введеному имени'
    
    # Constructor
    def __init__ (self,link_app):
        # Класс data_call имеет 1 атрибут 'link_app'
        self.link_app = link_app

    # Метод
    def search_data(self):
        sort_data = data.query("LInk == @self.link_app")
        print (sort_data)
        print("")
        
    # Метод
    def hello(self):
        print ('hello word !')
        print("")


    
        
