'''
1. Создать папку ./alphabet/ Если папка существует, то ОК.
2. В папке ./alphabet/ создать файлы
вида a.txt, b.txt, ..., z.txt
в которых будет записана строка алфавита,
но с заменой буквы из названия файла на прописную.
Пример: для b.txt строка будет aBcde...
3. Сделать щелчек Таноса - удалить случайным
образом половину всех файлов в этой папке.
'''

# path_win = r'C:\dir\dir2\dir3\file.txt'
# path_linux_macos_android_etc = r'/sda1/dir/di2/di3/file.txt'
#
# print(os.path.join('папка', 'файл'))  # os.path.join - создает адрес файла/папки по правилам ОС
# os.makedirs('files_test',
#             exist_ok=True)  # cоздает папку, в случае её наличия вернет ошибку, но существует ключ решающий   данную проблему
# with open(r'files_test\test.txt', 'w') as file:
#     pass
# print(os.listdir(r'C:\Users\Admin\PycharmProjects\PyBasic_1511'))  # просмотр содержимого папки(получим список)
# os.remove(r'files_test\test.txt')  # удаляет заданный файл
# os.rmdir('files_test')  # удаляет заданную папку
import os
import random
import string


# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(ord('A'))
# for i in range(65, 91):
#     print(chr(i), end='')
# my_alphabet = string.ascii_lowercase
# for symbol in my_alphabet:
#     text = my_alphabet.replace(symbol, symbol.upper())
#     print(text)

class PlayWithFolder:
    """
    Работа с тестовой папкой наполняемой автоматически,
     выборочное удаление элементов из папки
    """

    def __init__(self, dirname: str = 'alphabet'):
        """
        создание объекта = создание папки, по умолчанию имя папки alphabet
        :param dirname:
        """
        # задача 1
        self.dirname = dirname
        os.makedirs(dirname, exist_ok=True)

    def create_file(self, symbol: str):
        """
        создание файла в заданной папке (свойство dirname)
        имя передается в метод,
        генерируется строка в из символов алфавита, где symbol приводится к прописному виду
        :param symbol:
        :return:
        """
        # задача 2 (часть 1)
        file_path = os.path.join(self.dirname, f'{symbol}.txt')
        with open(file_path, 'w') as file:
            file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def create_files(self):
        """
        создает строку на основании которой будут созданы файлы
        :return:
        """
        for symbol in string.ascii_lowercase:
            self.create_file(symbol)

    def tanos_click(self):
        """
        удаление половины файлов из заданной папки
        файлы выбираются случайным образом
        :return:
        """
        directory_list = os.listdir(self.dirname)
        random.shuffle(directory_list)  # перемешиваем список
        for filename in directory_list[::2]:
            file_path = os.path.join(self.dirname, filename)
            os.remove(file_path)


# my_object = PlayWithFolder()
# my_object.create_files()
# my_object.tanos_click()
# my_object.tanos_click()

directory = 'files'
fi = 'files\London.txt'
print('os.path.isfile(directory) -> ', os.path.isfile(directory))
print('os.path.isfile(fi) -> ', os.path.isfile(fi))
print('os.path.isdir(directory) -> ', os.path.isdir(directory))
print('os.path.isdir(fi) -> ', os.path.isdir(fi))
'''
os.path.isfile(путь) - является ли заданный элемент файлом
os.path.isdir(путь) - является ли заданный элемент папкой
'''

