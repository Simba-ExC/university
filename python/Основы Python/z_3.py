month = str(input('Введите месяц: '))
date = int(input('Введите число: '))
if (month == ('январь') and date >= 21) or (month == ('февраль') and date <= 19):
    print ('Водолей')
elif (month == ('февраль') and date >= 20) or (month == ('март') and date <= 20):
    print ('Рыбы')
elif (month == ('март') and date >= 21) or (month == ('апрель') and date <= 20):
    print ('Овен')
elif (month == ('апрель') and date >= 21) or (month == ('май') and date <= 20):
    print ('Телец')  
elif (month == ('май') and date >= 21) or (month == ('июня') and date <= 21):
    print ('Близницы')  
elif (month == ('июня') and date >= 22) or (month == ('июля') and date <= 22):
    print ('Рак') 
elif (month == ('июля') and date >= 23) or (month == ('августа') and date <= 23):
    print ('Лев')
elif (month == ('августа') and date >= 24) or (month == ('сентября') and date <= 23):
    print ('Дева')        
elif (month == ('сентября') and date >= 24) or (month == ('октября') and date <= 23):
    print ('Весы')
elif (month == ('октября') and date >= 24) or (month == ('ноября') and date <= 22):
    print ('Скорпион') 
elif (month == ('ноября') and date >= 23) or (month == ('декабря') and date <= 21):
    print ('Стрелец')  
elif (month == ('декабря') and date >= 22) or (month == ('января') and date <= 20):
    print ('Стрелец')                         
else:
    print('Вывод {}')
