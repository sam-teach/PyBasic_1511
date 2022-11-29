i = int()
f = float()
s = str()
b = bool()
# type() - функция возвращающая тип переданной переменной
print(type(i))
print(type(f))
print(type(s))
print(type(b))
# неявное преобразование
result = 2 + 5
print(result, type(result))
result = 2 + 5.3
print(result, type(result))
result = 2 + True
print(result, type(result))
result = 2 + False
print(result, type(result))
print()
# явное преобразование
result = 2 + int(5.9)
print(result, type(result))
result = 2 + int('12')
print(result, type(result))
result = str(2) + '12'
print(result, type(result))
print()
# чуть-чуть строк
print('Hello')
print('Hello'+'world')
print('Hello'*6)
print(False*'world')

