import math
#Просим пользователя ввести x
x=int(input("Введите x:"))
#Просим пользователя ввести y
y=int(input("Введите y:"))
#Формула
f=abs(x**(y/x)-pow(y/x,(1/3))) +(y-x)
#Вывод результата
print(f)
