import random
L = random.sample(range(100), 8)
N = random.sample(range(100), 5)
M = random.sample(range(100), 5)
print ("созданны массивы\nL:",L,"\nN:",N,"\nM:",M)
numerator = sum(L);
numerator = numerator ** 2
denominator = sum(N)+sum(M)
denominator = denominator * L[1]
Z = numerator / denominator 
print ("Z =%.2f" %  Z)
