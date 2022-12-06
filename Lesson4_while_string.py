'''
while выражение:
    тело цикла
'''
# password = '123'
# pass_in = input('Введите пароль: ')
# while pass_in != password:
#     print('Неверно!')
#     pass_in = input('Попробуйте еще: ')
# print('Ура, получилось')

# password = '123'
# while True:
#     pass_in = input('Input password: ')
#     if pass_in == password:
#         break  # прерывает выполнение цикла
#     print('Wrong pass!')
# print('Ура')

# num = int(input('Input number: '))
# result = 0
# while num > 0:
#     result += num % 10  # result = result + num % 10
#     num = num // 10
# print(result)
#
# num2 = int(input('Input number: '))
# result = 0
# while num2 > 0:
#     result = result * 10 + num2 % 10
#     num2 = num2 // 10
# print(result)

# for h in range(5):
#     for w in range(5):
#         print('*', end=' ')
#     print()
# print()
# for h in range(5):
#     for w in range(h+1):
#         print('*', end=' ')
#     print()
# print()
# for h in range(5, 0, -1):
#     for w in range(h ):
#         print('*', end=' ')
#     print()
#            012345
my_string = 'string'
my_string2 = "another string"
my_string3 = '''multiline 
string'''
print(len(my_string))
print(my_string[0])  # обращение по индексу
print(my_string[-1])  # отрицательные индексы обращаются конца строки
# срезы
# string[старт:стоп:шаг] default[0,len(string),1]
print(my_string)
print(my_string[2:])
print(my_string[:4])
print(my_string[1:4])
print(my_string[4:1:-1])
print(my_string[::-1])
i = 123456
i = int(str(i)[::-1])
print(type(i), i)
# string (тип данных строка) - НЕИЗМЕНЯЕМЫЙ тип данных
# my_string[3]='o' #TypeError: 'str' object does not support item assignment
# del(my_string[3]) #TypeError: 'str' object doesn't support item deletion
my_string = 'some new string'
print(my_string)

print(my_string.split())
print(my_string.split(sep='s'))
print(my_string.upper())
print(my_string)
symbol = '1'
print(symbol.isdigit())
print(symbol.isalpha())
print(symbol.isalnum())
print(my_string2)
print(my_string2.find('t'))
print(my_string2.find('tr'))
print(my_string2.find('k'))

print(my_string2.replace('i', 'O'))
print(my_string)
print(my_string.replace('s', '***'))

print('{}, {}, {}')
print('{}, {}, {}'.format(12, 'Apple', 'сорок два'))
print('{1}, {2}, {0}'.format(12, 'Apple', 'сорок два'))
print('{c}, {a}, {b}'.format(a=12, b='Apple', c='сорок два'))


