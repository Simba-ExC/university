stamp=[]
carrying=[]
plate=[]
for i in range(2):
    spisok = input ("введите марку , грузоподъемность и номер автомобиля \n")
    car = spisok.split(" ")
    stamp.append(car[0])
    carrying.append(car[1]) 
    plate.append(car[2])
print ("текущие машины: \n Марка - ",stamp,"\n Грузоподъемность - ",carrying ,"\n Номер машины - ",plate)
