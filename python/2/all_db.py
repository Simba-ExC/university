import pandas as pd
import numpy as np

data = pd.read_csv('Contacts_sample.csv', delimiter=';') # записываем из файла в DataFrame

#полиморфизм
class get_bd():
    # Метод
    #полиморфизм
    def greeting(self):
        print ("База данных имеет вид")
        print (data)





