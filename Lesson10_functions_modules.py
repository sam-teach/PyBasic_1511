# '''
# HW
# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#     а) Создать список и поместить туда имя самого молодого человека.
#         Если возраст совпадает - поместить все имена самых молодых.
#     б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
#     в) Посчитать среднее количество лет всех людей из начального списка.
# '''
# peoples_list = [
#     {"name": "John", "age": 15},
#     {"name": "Jack", "age": 45},
#     {"name": "Any", "age": 24},
#     {"name": "Mary", "age": 16},
#     {"name": "Nick", "age": 35},
#     {"name": "John2", "age": 15},
# ]
#
# min_age = 1110
# # for i in peoples_list:
# #     if min_age > i['age']:
# #         min_age = i['age']
# # result_list = []
# l = min([i['age'] for i in peoples_list])
# result = [i['name'] for i in peoples_list if i['age'] == l]
# print(result)
# # for i in peoples_list:
# #     if min_age == i['age']:
# #         result_list.append(i['name'])
# # print(result_list)

'''
def имя_функции(аргумент(ы)):
    """строка документации"""
    тело функции (операторы)(код)
'''


def function_name():
    """описание функции"""
    pass


def print_hello():
    '''печатает hello'''
    print('hello')


def print_named_hello(name):
    '''печатает именованное приветствие'''
    print(f'Hello my dear {name}')


def get_named_hello(name: str) -> str:
    '''возвращает именованное приветствие'''
    return f'Hello my dear {name}'


def calc(num1, op: str, num2):
    return eval(f'{num1}{op}{num2}')


print_hello()
print_named_hello('Vasiliy')
named_hello = get_named_hello('Vasiliy')
print(type(named_hello), named_hello)
print(calc(3.2, '+', 5))
print(get_named_hello.__doc__)
