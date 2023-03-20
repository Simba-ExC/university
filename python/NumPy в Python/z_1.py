import numpy as np
num = input("Введите N:")
num = int (num)

a = np.zeros ((num))
for i in range (num):
    num = num -1
    a [i] = num
print(a)

