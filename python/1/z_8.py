import random
print ("введите размеры матрицы")
M= int (input("Введите M = "))
N= int (input("Введите N = "))
matrix = [[random.randrange(-10,10) for y in range(M)] for x in range(N)]

for row in matrix:
    for item in row:
        if item >= 0:
            item_s= str(item)
            item_f =' '
            item_f = item_f + item_s
            print(item_f, end=' \t')
        else:
            print(item, end=' \t')
    print()

min = matrix[0][0]
M_min = 0
N_min = 0
for i in range(M):
    for j in range(N):
        if(matrix[i][j]<min):
            min=matrix[i][j]
            M_min = i 
            N_min = j
print("минимальное значение: ",min," в позиции M=",M_min+1 , "N=",N_min+1 )
for i in range(M):
    for j in range(N):
        if(matrix[i][j]== 0):
            sum_j = 0
            print ("ноль в ячейке",i+1,j+1)
            for a in range(N):  
                sum_j = sum_j + matrix[i][a]
            matrix[i][j]= sum_j
for row in matrix:
    for item in row:
        if item >= 0:
            item_s= str(item)
            item_f =' '
            item_f = item_f + item_s
            print(item_f, end=' \t' )
        else:
            print(item, end=' \t')
    print()








