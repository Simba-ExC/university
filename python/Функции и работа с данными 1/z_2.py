import numpy as np
import pandas as pd
data = pd.read_csv('keywords.csv', delimiter=',') # записываем из файла в DataFrame 

entry = 0           # вспомогательная переменная для 

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

nmp = geo_data.to_numpy() # делаем из DataFrame массив , так удобнее

for i in range(data.shape[0]): 
    row1 = data.iloc[[i]]           # разбиваем на строки
    row2 = row1[['keyword']]        # выбираем нужную нам колонку
    entry = 0                       # обнулем переменную
    for r in range ( len(nmp) ):
        for c in range ( len(nmp[r]) ):
            
            if (row2 == nmp[r][c] and entry == 0 ):     # сравниваем каждый элемент массива с keyword из DataFrame который состоит из файла keywords.csv
                df['region'] = region.apply(nmp[r][0])
                entry == 1                              # если встрелся город , записываем в колонку region, регион который находтся в нулевой колонке и присваем переменной значение 2, что не делать поиск повторно.

            elif (entry == 0 and row2 != nmp[2][3]):    # если в самом конце последний элемент масива не подходит и до этогоо небыло вхождений , следовательно список закончен и поисковый запрос не содержит названия города
                df['region'] = "undefined"              
