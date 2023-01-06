# '''
# open(имя_файла, режим открытия)
#     путь в ОС   r - read - открывает файл для чтения(курсор в начале файла) если файл не существует - ошибка
#                 w - write - открывает файл для записи, СТИРАЯ ВСЕ СОДЕРЖИМОЕ. Если файл не существует - создаст его
#                 a - append - открывает файл для чтения и записи(курсор в КОНЦЕ файла) если файл не существует - создаст его
# функция open возвращает объект для работы с файлом
# после окончания работы с файлом его необходимо закрыть с помощью метода close()
# '''
# my_file = open('files/test.txt', 'w')
# print(type(my_file))
# print(my_file.name)
# my_file.close()
#
# '''
# менеджер контекста следит за открытым файлом и закрывает его как только код выходит за пределы области видимости
# это может происходить как во время нормальной работы программы так и при появлении ошибок
# '''
# with open('files/test.txt', 'w') as my_file:
#     print(type(my_file))
#     print(my_file.name)
# print()

# '''
# запись в файл
# '''
# with open('files/test.txt', 'w') as file:
#     file.write('очень важная строка\n')
#
# with open('files/test.txt', 'a') as file:
#     file.write('еще одна очень важная строка\n')

'''
чтение из файла
'''

with open('files/test.txt', 'r') as file:
    print('read')
    result = file.read()
    print(result)

with open('files/test.txt', 'r') as file:
    print('readline')
    result = file.readline()
    print(result)

with open('files/test.txt', 'r') as file:
    print('readlines')
    result = file.readlines()
    print(result)

with open('files/test.txt', 'r') as file:
    print('read(4)')
    result = file.read(4)
    print(result)

with open('files/test.txt', 'r') as file:
    print('for')
    for line in file:
        print(line,end='')
