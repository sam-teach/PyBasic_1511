'''
OOP
'''


# # класс - пользовательский тип данных
# class Student:
#     '''documentation'''
#     # переменные в классе - атрибуты/свойства/поля
#     name: str = 'Test'
#     age: int = 0
#
#     # функция - метод
#     # self - указатель содержащий адрес объекта являющегося инициатором вызова данного метода
#     def print_data(self):
#         # обращение к свойствам объекта происходит через указатель self
#         print(f'{self.name} {self.age}')
#
#
# variable = Student()
# print(variable.age)
# variable.print_data()
# variable.age = 789
#
# variable.gender = 'female'
# print(variable.gender)
#
# variable2 = Student()
# print(variable2.__doc__)
# print(variable2.__dir__())  # список атрибутов и методов объекта
# print(variable.__dict__)  # список атрибутов заданных в объекте

class Student:
    id = 0
    age = 0
    name = ''
    gender = ''

    def __init__(self, name: str = 'Taras', age: int = 21, gender: str = 'male'):
        self.name = name
        self.age = age
        self.gender = gender
        print('Construct student is done!')

    def __str__(self):
        '''
        some string
        :return:
        '''
        return f'{self.name}, {self.age}, {self.gender}'

    def __int__(self):
        return 42


s = Student('Mary', 14, 'it')
s2 = Student()
print(s)
print(s.__str__())
print(int(s))
print(s.__getattribute__('age'))
print(str(s2))
print(int(s) + int(s2))
