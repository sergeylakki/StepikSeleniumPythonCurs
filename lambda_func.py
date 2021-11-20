func = (lambda x,y,z : x+y+z) (3,5,6)#Создание лабда функции и вызов
print(func)
func2 = (lambda x,y,func3 : x+y+func3(x+y,x-y)) (3,5,lambda x,b : x-b )#Создание и вызов ламбда функции и передача в качестве параметра другой ламбда функции
print(func2)
func4 = lambda x,y,func3 : x+y+func3#Создание именовоной ламбда функции
print(func4(3,8,9))

import dis
print("labda:")
add = lambda x, y: x+y
type(add)
dis.dis(add)
add
print("func:")
def add2(x, y): return x+y
type(add2)
dis.dis(add2)
add2

