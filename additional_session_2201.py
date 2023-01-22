'''Марія Корольова'''


# Функции в отдельном модуле, проверка работоспособности в main
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.

def random_words(my_list):
    new_list = []
    # for i in my_list[n:(len(my_list) + 1)]: <---
    for n in range(len(my_list)):
        if n % 2 == 0:
            new_list.append(my_list[n][::-1])
        else:
            new_list.append(my_list[n])

    return new_list


# my_list = input('Введите любое слово: ').split(', ')
# new_list = []
# print(random_words(my_list))
# print()


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# лементы из my_list у которых первый символ - буква "a".

def random_list(my_list):
    new_list = []
    # for i in my_list[:(len(my_list) + 1)]: <---
    for i in my_list:
        if i[0] == 'a' or i[0] == 'A':
            new_list.append(i)
    return new_list


# my_list = input('Введите любое слово: ').split(' ')
# new_list = []
# print(random_list(my_list))
# print()


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

def random(my_list):
    new_list = []
    # for i in my_list[:(len(my_list) + 1)]: <---
    for i in my_list:
        if 'a' in i or 'A' in i:
            new_list.append(i)
    return new_list


# my_list = input('Введите любое слово: ').split(' ')
# new_list = []
# print(random(my_list))
# print()


# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

def random(
        my_list):  # называть  функцию так же как и встроенный инструмент означает невозможность использования встроенного иструмента
    new_list = []
    # for i in my_list[:(len(my_list) + 1)]: <----
    for i in my_list:
        try:
            i = int(i)
        except:
            new_list.append(i)
            continue
    return new_list


# ---teacher case
def get_strings_from_list(my_list: list) -> list:
    """
    получение списка строк из списка my_list
    :param my_list:
    :return: список строк
    """
    result_list = []
    for element in my_list:
        # if type(element)==str:
        if isinstance(element, str):
            result_list.append(element)
    return result_list


# my_list = input('Введите любое слово: ').split(' ')
# new_list = []
# print(random(my_list))
# print()


# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

def random(my_str):  # повторяющееся имя, встроенное имя
    my_list = list(my_str)
    for i in my_list:
        if my_list.count(i) == 1:
            unique_list.append(i)
    return unique_list


# teacher case
def uniq_symbols_from_string(my_str: str) -> list:
    """
    получение списка уникальных символов из строки
    :param my_str:
    :return:
    """
    result_list = []
    for symbol in my_str:
        if my_str.count(symbol) == 1:
            result_list.append(symbol)
    return result_list


print('--------\n', uniq_symbols_from_string('aaasdddfggg'))


# my_str = input('Введите строку: ')
# unique_list = []
# print(random())
# print()


# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

def random_uni(my_str1, my_str2):
    # my_list = list(my_str1)
    # my_list2 = list(my_str2)
    unique_list = []
    for i in my_str1:
        if i in unique_list:
            continue
        if i in my_str2:
            unique_list.append(i)

    return unique_list


print(random_uni('abcade', 'ahjkl'))


string.as

def get_common_symbols(my_str1: str, my_str2: str) -> list:
    result_list = list(set(my_str1).intersection(set(my_str2)))
    return result_list


print(get_common_symbols('abcade', 'ahjbkl'))


# my_str1 = input('Введите строку: ')
# my_str2 = input('Введите строку: ')
# unique_list = []
# print(random(my_str1, my_str2))
# print()


# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

def random(my_str1, my_str2):
    my_list = list(my_str1)
    my_list2 = list(my_str2)
    unique_list=[]
    for i in my_list:
        count_i = my_list.count(i)
        if count_i == 1:
            if i in my_list2:
                count_i = my_list2.count(i)
                if count_i == 1:
                    unique_list.append(i)
        # else:
        #     count_i = 0
    return unique_list


# my_str1 = input('Введите строку: ')
# my_str2 = input('Введите строку: ')
# unique_list = []
# print(random(my_str1, my_str2))
# print()

# *8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
