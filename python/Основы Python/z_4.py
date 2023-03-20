width = int(input('Введите ширину: '))
length = int(input('Введите длину: '))
height = int(input('Введите высоту: '))

if (length >= 200  ):
    print ('Упаковка для лыж')
elif ((width >= 15) and (width <= 50)) or ((length >= 15) and (length <= 50) ) or ((height >= 15) and (height <= 50) ):
    print ('Коробка №2')
elif (width <= 15 ) or (length <= 15) or (height <= 15):
    print ('Коробка №1')
else:
    print ('Стандартная коробка №3')
