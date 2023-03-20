import math
x1 = int (input ("введите x1 \nx1="))
x2 = int (input ("введите x2 \nx2="))
x3 = int (input ("введите x3 \nx3="))
sp = [x1,x2,x3]
x_min = min(sp)
x_max = max(sp)
a= x_max/2
b= (x_min**3)-((x1+x2)/3)
print ("a=",a,"\nb=",b)
