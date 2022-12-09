# # проверка, является ли число простым
# number = int(input('Input number: '))
# for i in range(2, number // 2 + 1):
#     if number % i == 0:
#         print('Число не простое')
#         break
# else:
#     # этот блок выполнится только если цикл завершился сам,
#     # без прерывания(break)
#     print('число простое')

# создание списка
# my_list = list()
# my_list2 = []
# my_list3 = [1, 2, 3, 'VASA', 5.2, my_list]
# my_list4 = list('qwerty')
# print('my_list', my_list)
# print('my_list2', my_list2)
# print('my_list3', my_list3)
# print('my_list4', my_list4)
# my_list5 = list(my_list3) + my_list4
# print('my_list5',my_list5)

# обращение к элементам
#     0  1  2  3  4  5 0    1    2     6
# li = [1, 2, 3, 4, 5, ['a', 'b', 'c'], 'Anna']
# print(li[5])
# print(li[5][1])  # список в списке
# print(li[3:6])  # срезы
# size = len(li)
# print(size)
# print(li[-2])  # отрицательный индекс позволит обращаться с конца списка
# # перебор списка по индексу
# for i in range(len(li)):
#     print(li[i], end=' ')
# print()
# # перебор списка по элементно
# for i in li:
#     print(i, end=' ')
# print()
# # перебор списка по индексу
# i = 0
# while i < len(li):
#     print(li[i], end=' ')
#     i += 1
# print()

# изменение списка
# li = [1, 2, 3, 4, 5, 6]
# print(li)
# li[3] = 999
# print(li)
# li[1:4] = [111, 222]
# print(li)
# # li[::2]=[5,55,555]
# # print(li)
# li[2], li[3] = li[3], li[2]
# print(li)

# методы списков
# li = [1, 4, 2, 6, 2, 7, 2, 9, 5]
# # добавление элемента
# li.append('blabla')
# print(li)
# # вставляет по индексу переданный элемент
# li.insert(3, [1, 2, 3])
# print(li)
# # возвращает индекс первого совпавшего элемента
# print(li.index(2))
# # возвращает количество совпадающих с переданным элементов
# print(li.count(2))
# # сортировка списка(reverse-обратная)
# # li.sort(reverse=True)
# # print(li)
# import copy
# li2 = copy.deepcopy(li)
# print('li', li)
# print('li2', li2)
# li[4:8] = [1]
# print('li', li)
# print('li2', li2)
# li[3][1] = 777
# print('li', li)
# print('li2', li2)

# генераторы списков
from random import randint

li = [i for i in range(20)]
print(li)
li2 = [i * 2 for i in range(20)]
print(li2)
li3 = ['vasa' for i in range(20)]
print(li3)
li4 = [randint(1, 100) for i in range(20)]
print(li4)
li5 = [randint(1, 100) for i in range(20) if i % 2 == 0]
print(li5)
