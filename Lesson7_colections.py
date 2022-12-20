'''
Кортеж - тип данных, является НЕИЗМЕНЯЕМЫМ списком
'''
tu = tuple([1, 2, 3, 4])
tu2 = ('1', 2.3, 4, 'Anatoliy')
tu3 = tuple('Game')
print(tu)
print(tu2)
print(tu3)
tu4 = (1, 2, 3, ['q', 'w', 'e', 'r'])
print(tu4)
tu4[3][1] = 1234
print(tu4)
