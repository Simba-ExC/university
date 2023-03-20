import math
a = int (input ("введите a \na="))
b = int (input ("введите b \nb="))
x = ((a+b)/((2*a)-b))*(a+b)
L=(math.sqrt(abs(x-a)))* math.cos(math.pi/6)
print ("x=",x," L=",L)
