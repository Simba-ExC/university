import random
A = random.sample(range(10), 10)
C = random.sample(range(10), 10)
P = int (input ("введите P \nP="))
print ("создан массив\nA:",A)
print ("\n\nсоздан массив\nC:",C)
D=[]


d1 = []
for j in range(5):
    d2 = []
    for i in range(5):
        if A[i] < P:
        d2.append(A[i])   
    d1.append(d2)
    
        
print ("Полученная массив: ")
for w in range(len(D)):
    for s in range(len(D[w])):
        print(D[w][s],end=" ")
    print()


    
