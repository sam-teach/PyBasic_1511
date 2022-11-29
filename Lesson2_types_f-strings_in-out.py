from math import sqrt

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
print('Hello' + 'world')
print('Hello' * 6)
print(False * 'world')
# операторы
'''
арифметические
+ - сложение
- - вычитание
* - произведение
/ - деление
** - возведение в степень
// - деление нацело(без остатка) только int
% - получение остатка(без целой части) только int
= - присвоение ("копирование" справа налево)
'''
a = 3
b = 5
a = b
print(a, b)
print(17 // 3)
print(17 % 3)
print(sqrt(17))
print()
'''
логические
> - левое больше правого
< - левое меньше правого
>= - левое больше либо равно правого
<= - левое меньше либо равно правого
== - левое равно правому
or - вернет истину если левое ИЛИ правое истина
and - вернет истину если левое И правое истина
^(xor) - вернет истину если ЛИБО левое ЛИБО правое истина
not  - вернет истину если элемент ложь 
in - вернет истину если элемент слева принадлежит элементу справа
'''
print('or')
print(True or False)
print(2 == 2.0 or 4 > 8)
print(2 > 2.0 or 4 > 8)
print('and')
print(True and False)
print(2 == 2.0 and 4 > 8)
print(2 > 2.0 and 4 > 8)
print(2 == 2.0 and 4 < 8)
print('xor')
print(True ^ False)
print((2 == 2.0) ^ (4 > 8))
print((2 > 2.0) ^ (4 > 8))
print((2 == 2.0) ^ (4 < 8))
print('not')
print(not True)
print(not 2 == 2.0)
print(not 4 > 8)
print('in')
print('a' in 'Anton')
print('a' in 'Mila')
print('-----------f-строки-----------')
age = 12
name = 'Taras'
hello_message = f'Привет {name}, тебе действительно {age} лет?'
print(hello_message)
old_hello_message = 'Привет ' + name + ', тебе действительно ' + str(age) + ' лет?'
print(old_hello_message)
print('in/out')
# input() - функция возвращающая данные введенные с клавиатуры в виде СТРОКИ
# input('напиши что нибудь') - выведет в консоли приглашающее сообщение
# name = input('Введи свое имя: ')
# age = int(input('Введи свой возраст: '))
# print('name', name, type(name))
# print('age', age, type(age))

# примеры
a = float(input("Введите а: "))
b = float(input("Введите b: "))
print(f'{a} + {b} = {a + b}')

r = float(input('Введите радиус окружности: '))
print(f'Длиннa окружности {3.14 * r ** 2}')

number = int(input('Введите целое трехзначное число: '))
print(
    f'В этом числе '
    f'{number % 10} единиц,'
    f' {number // 10 % 10} десятков, '
    f'{number // 100} сотен'
)

