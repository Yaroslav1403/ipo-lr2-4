import math
x=int(input("Введите x:"))
y=int(input("Введите y:"))
f=abs(x**(y/x)-pow(y/x,(1/3))) +(y-x)
print(f)