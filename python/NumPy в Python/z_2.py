from random import randint
 
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
 
matrix = [[randint(-(n + m), (n + m)) for j in range(m)] for i in range(n)]
 
n = len(matrix)
m = len(matrix[0])
# I
diag_sum = 0
 
if(n == m):
    i = 0
    while i < n - 1:
        diag_sum = diag_sum + matrix[i][i + 1]
        i = i + 1
 
elif(n > m):
    i = 0
    while i < n - m + 1:
        diag_sum = diag_sum + matrix[i][i + 1]
        i = i + 1
 
elif(m > n):
    i = 0
    while i < m - n + 1:
        diag_sum = diag_sum + matrix[i][i + 1]
        i = i + 1
print(" ")
print(matrix)
print(" ")
print("сумма элементов заглавной диагонали: " + str(diag_sum))
 
