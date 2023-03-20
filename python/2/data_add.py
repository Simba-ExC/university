import pandas as pd
import numpy as np

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame


class data_add:
    'добавляем магазин'
    
    # Constructor
    def __init__ (self,link_app,Contact_app, tupe_app):
        self.link_app = link_app # передаем название 
        self.Contact_app = Contact_app # передаем контакты
        self.tupe_app = tupe_app # тип контакты ( мыло или телефон )
        count_row = data.shape[0] + 1 # весь список и добавляем в конец
        count_id = data['ID'].max()+ 1 # добавляем последний ID 
        count_sitesid = data['SiteID'].max()+ 1 # последнее id сайта
        data.loc[count_row] = [count_id, count_sitesid, self.link_app, self.Contact_app, self.tupe_app ]
        sort_data = data.query("ID == @count_id") #
        print ("")
        print ("добавлена запись")
        print (sort_data)
        print ("")
    # Метод
    #полиморфизм
    def greeting(self):
        print (data)

