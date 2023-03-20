import numpy 
countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
i = 0
print('Средняя температура в странах:')
i=0
while i < 4:
    a=[countries_temperature[i][1]]
    z=numpy.mean(a)
    print(countries_temperature[i][0],'=',(z - 32) * 5 / 9,'C')
    i+=1



