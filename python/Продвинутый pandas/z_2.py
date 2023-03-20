import numpy as np
import pandas as pd

data = pd.read_csv('keywords.csv', delimiter=',') # записываем из файла в DataFrame
data.insert(2, "region", "unidentified")
entry = 0           # вспомогательная переменная для 

geo_data = {
'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}
for r in range (3):
    for c in range (2):
        name = list(geo_data.items())[r][c]
        sort = data.query("keyword == @name")
        for r in range (len(sort)):
            row1 = sort.iloc[[r]]
            row2 = row1.iloc[0].values
            print ("есть вхождение в строке : ", row2,"добавим",list(geo_data.items())[r][0])
            data.loc[data['shows'] == row2[r], 'region' ] = list(geo_data.items())[r][0]

