'''
Кортеж - тип данных, является НЕИЗМЕНЯЕМЫМ списком
'''
# tu = tuple([1, 2, 3, 4])
# tu2 = ('1', 2.3, 4, 'Anatoliy')
# tu3 = tuple('Game')
# print(tu)
# print(tu2)
# print(tu3)
# tu4 = (1, 2, 3, ['q', 'w', 'e', 'r'])
# print(tu4)
# tu4[3][1] = 1234
# print(tu4)
'''
множество - неупорядоченный набор уникальных элементов
'''
# my_set = set([1, 2, 33, 4, 33, 6])
# print(my_set)
# # добавлени
# my_set.add('Vasilisa')
# my_set.add('Vasa')
# my_set.add('Maria')
# my_set.add('Vasa')
# print(my_set)
# my_set.update((1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(my_set)
# my_set.update('Katarina')
# print(my_set)
# # удаление
# my_set.discard('Vasilisa')
# print(my_set)
# # discard - исключает элемент, в случае отсутствия нет ошибки
# my_set.discard('Vasya')
# print(my_set)
# # remove - удаляет элемент, в случае отсутствия будет ошибка
# my_set.remove(1)
# print(my_set)
'''
практика
'''
from random import randint

# ---Дано целое число, посчитать количество нулей в нем
# num = randint(99, 99999)
# print(num)
# count_zero = 0
# for sym in str(num):
#     if sym == '0':
#         count_zero += 1  # count_zero = count_zero + 1
# print(count_zero)
# # python style
# print(str(num).count('0'))

# ---Дано целое число, определить количество нулей в конце числа. Например: 10203000 - 3 нуля
num = 10203000
print(num)
count_zero = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    count_zero += 1
print(count_zero)
# вариант 2
# count_zero = 0
# while num > 0:
#     if num % 10 != 0:
#         break
#     count_zero += 1
#     num //= 10
# print(count_zero)
# типа python style
# print(len(str(num)))
# print(len(str(int(str(num)[::-1]))))
print(len(str(num)) - len(str(int(str(num)[::-1]))))
