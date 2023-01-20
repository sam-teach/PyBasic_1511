# class User:
#     # __ (два нижних подчеркивания) перед именем атрибута делают его скрытым за пределами класса(private)
#     __name = str()
#     __age = int()
#     __skills = list()
#
#     def __init__(self, name: str, age: int = 18):
#         self.__name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Name: {self.__name}, age: {self.__age}'
#     # методы позволяющие работать с private атрибутами называются акцесорами
#     # меняющие private атрибут называются сеттерами
#     # def set_age(self, age: int):
#     #     if age >= 0:
#     #         self.__age = age
#     #
#     # возвращающие private атрибут называются геттерами
#     # def get_age(self):
#     #     return self.__age
#     # Аннотации атрибутов создаются с помощь @property, позволяют получать доступ к private атрибуту через псевдоним
#     # при этом технически отрабатывает метод
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     # аннотация сеттера не может быть описана выше аннотации геттера
#     @age.setter
#     def age(self, age: int):
#         if age >= 0:
#             self.__age = age
#
#     @property
#     def skills(self):
#         return self.__skills.copy()
#
#
# obj = User('Anton')
# print(obj)
# # obj.__age = -12
# # print(obj)
# # print(obj.__age)
# # obj.set_age(-12)
# obj.age = -234
# print(obj)
# print(obj.age)
# # print(obj.get_age())
# li = obj.skills
# print(li)
# li.append(123)
# print(li)
# print(obj.skills)

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return f'Name: {self.name}'


class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def __str__(self):
        return f'Name: {self.name}'


class Employee2(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def __str__(self):
        return f'{super().__str__()}, Position: {self.__position}'


obj = Employee2('Taras', 'Contrabas')
print(obj.name)
