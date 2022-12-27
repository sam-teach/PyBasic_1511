# '''
# *4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого
#  первый элемент из my_list стоит на последнем месте.
#  Если my_list [1,2,3,4], то new_list [2,3,4,1]
# '''
# my_list = [1, 2, 3, 4]
# new_list = []
# for i in my_list:
#     new_list.append(i)
# new_list.append(new_list.pop(0))
# print(new_list)
# # ------
# new_list = my_list[1:] + my_list[0:1]
# print(new_list)

# '''
# 5. Дан список my_list. В ЭТОМ списке первый элемент переставить
#  на последнее место.[1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя! (используйте метод pop)
# '''
# my_list = [1, 2, 3, 4]
# my_list.append(my_list.pop(0))
# print(my_list)

# '''
# 6. Дана строка в которой есть числа (разделяются пробелами).
#  Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
# (используйте split и проверку isdigit)
# '''
# # my_str = '43 больше чем 34, но меньше чем 56'
# # sum = 0
# # for word in my_str.split():
# #     if word.isdigit():
# #         sum += int(word)
# #     else:
# #         var = word
# #         for index in range(len(var)):
# #             if not var[index].isalnum():
# #                 var.replace(var[index], ' ')
# #         print(var)
# #         for w in var.split():
# #             if w.isdigit():
# #                 sum += int(w)
#
# # print(sum)
#
#
# # li = [expression for item in iterable if condition]
# # expression - выражение
# # item - элемент извлекаемый из последовательности
# # iterable - последовательность
# # condition - условная конструкция, добавление єлемент произойдет только если она вернет True
#
# st_1 = "'43 больше чем 34,3 но меньше чем 56'"
# st_2 =''
# mus = []
# for x in st_1:
#     if x.isdigit():
#         st_2 += str(x)
#     else:
#         st_2 += ' '
# print(st_2)
# print(sum([int(x) for x in st_2.split()]))
#
# s = sum([int(word) for word in st_1.split() if word.isdigit()])

# '''
# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа
#  l_limit и r_limit, которые точно находятся в
# этой строке. Причем l_limit левее чем r_limit. В переменную sub_str
#  поместить НАИБОЛЬШУЮ часть строки между этими
#  символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
# '''
# my_str = 'My long string'
# l_limit = "o"
# r_limit = "g"
# sub_str=my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit)]
# print(sub_str)
#
# my_str = 'My long string'
# l_limit = 'o'
# r_limit = 'g'
# sub_str = ''
# for len_l in range(len(my_str)):
#     if my_str[len_l] == l_limit:
#         index_l = len_l + 1
#         break
# for len_r in range(-1, len(my_str)):
#     if my_str[len_r] == r_limit:
#         index_r = len_r
#         break
# sub_str = my_str[index_l:index_r]
# print(sub_str)

# '''
# 8. Дана строка my_str.
#  Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
#  содержит нечетное количество символов, пропущенный второй
#  символ последней пары должен быть заменен
#  подчеркиванием ('_').
#  Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)
# '''
# my_str = 'abcde'
# my_list = ([my_str[i:i + 2] for i in range(0, len(my_str), 2)])
# if len(my_list[-1]) < 2:
#     my_list[-1] += '_'
# print(my_list)

# '''
# 9. Дан список чисел. Определите, сколько в этом списке элементов, которые больше суммы двух своих соседей
#  (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются,
#   поскольку у них недостаточно соседей. Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
# '''
# li = [2, 4, 1, 5, 3, 9, 0, 7]
# s = 0
# for i in range(1, len(li) - 1):
#     if li[i] > (li[i - 1] + li[i + 1]):
#         s += 1
# print(s)
#
# print(sum([1 for i in range(1, len(li) - 1) if li[i] > (li[i - 1] + li[i + 1])]))

# '''
# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33] Создать новый список в который поместить только строки из my_list.
# '''
# li = [1, 2, 3, "11", "22", 33]
# new_li = []
# for i in li:
#     # if isinstance(i, str):
#     if type(i) == str:
#         new_li.append(i)
# print(new_li)
#
# print([i for i in li if isinstance(i, str)])

# '''
# 12. Даны две строки. Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.
# '''
# my_str1 = 'qwerty'
# my_str2 = 'qazwsxedc'
# print(list(set(my_str1+my_str2)))

'''
13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках, но в каждой
 ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
  т.к. эти символы есть в каждой строке по одному разу
'''

my_str1 = 'aaaasdf1'
my_str2 = 'asdfff2'
# print(list(set(my_str1).intersection(set(my_str2))))
li1 = [i for i in my_str1 if my_str1.count(i) == 1]
li2 = [i for i in my_str2 if my_str2.count(i) == 1]
print(li1, li2)
print(set(li1) & set(li2))
li = set([i for i in my_str1 if my_str1.count(i) == 1]) & set([i for i in my_str2 if my_str2.count(i) == 1])
