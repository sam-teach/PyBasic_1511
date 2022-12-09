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
my_list = list()
my_list2 = []
my_list3 = [1, 2, 3, 'VASA', 5.2, my_list]
my_list4 = list('qwerty')
print('my_list', my_list)
print('my_list2', my_list2)
print('my_list3', my_list3)
print('my_list4', my_list4)
my_list5 = list(my_list3) + my_list4
print('my_list5',my_list5)
