import numpy as np
import pandas as pd
data = pd.read_csv('movies.csv', delimiter=',') # записываем из файла в DataFrame 

entry = 0           # вспомогательная переменная 
rating_data = {
'низкий рейтинг': [2],
'средний рейтинг': [4],
'высокий рейтинг': [5]
}

#nmp = rating_data.to_numpy() # делаем из DataFrame массив , так удобнее

for i in range(data.shape[0]): 
    row1 = data.iloc[[i]]           # разбиваем на строки
    #row2 = row1[['rating']]        # выбираем нужную нам колонку
    entry = 0                       # обнуляем переменную

    for r in range ( len(rating_data) ):
        print ("len(rating_data)",len(rating_data[1]))
        for c in range ( len(rating_data[r]) ):
            
            if (row1[['rating']] <= rating_data[r][c] and entry == 0    ):
                print ("row1[['rating']]",row1[['rating']])
                df['classs'] =  classs.apply(rating_data[r][0])
                entry == 1  
            elif ( entry == 0 & row1[['rating']] != rating_data[2][3]): # если в самом конце последний элемент масива не подходит и до этогоо небыло вхождений , следовательно список закончен и поисковый запрос не содерэит оценки фильма
                df['classs'] = "undefined" 
