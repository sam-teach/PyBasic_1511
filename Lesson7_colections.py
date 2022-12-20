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
my_set = set([1, 2, 33, 4, 33, 6])
print(my_set)
# добавлени
my_set.add('Vasilisa')
my_set.add('Vasa')
my_set.add('Maria')
my_set.add('Vasa')
print(my_set)
my_set.update((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(my_set)
my_set.update('Katarina')
print(my_set)
# удаление
my_set.discard('Vasilisa')
print(my_set)
# discard - исключает элемент, в случае отсутствия нет ошибки
my_set.discard('Vasya')
print(my_set)
# remove - удаляет элемент, в случае отсутствия будет ошибка
my_set.remove(1)
print(my_set)
