'''

'''


# класс - пользовательский тип данных
class Student:
    '''documentation'''
    # переменные в классе - атрибуты/свойства/поля
    name: str = 'Test'
    age: int = 0

    # функция - метод
    # self - указатель содержащий адрес объекта являющегося инициатором вызова данного метода
    def print_data(self):
        # обращение к свойствам объекта происходит через указатель self
        print(f'{self.name} {self.age}')


variable = Student()
print(variable.age)
variable.print_data()
variable.age = 789

variable.gender = 'female'
print(variable.gender)

variable2 = Student()
print(variable2.__doc__)
print(variable2.__dir__())  # список атрибутов и методов объекта
print(variable.__dict__)  # список атрибутов заданных в объекте
