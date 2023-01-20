class User:
    # __ (два нижних подчеркивания) перед именем атрибута делают его скрытым за пределами класса(private)
    __name = str()
    __age = int()
    __skills = list()

    def __init__(self, name: str, age: int = 18):
        self.__name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.__name}, age: {self.__age}'
    # методы позволяющие работать с private атрибутами называются акцесорами
    # меняющие private атрибут называются сеттерами
    # def set_age(self, age: int):
    #     if age >= 0:
    #         self.__age = age
    #
    # возвращающие private атрибут называются геттерами
    # def get_age(self):
    #     return self.__age
    # Аннотации атрибутов создаются с помощь @property, позволяют получать доступ к private атрибуту через псевдоним
    # при этом технически отрабатывает метод
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    # аннотация сеттера не может быть описана выше аннотации геттера
    @age.setter
    def age(self, age: int):
        if age >= 0:
            self.__age = age

    @property
    def skills(self):
        return self.__skills.copy()


obj = User('Anton')
print(obj)
# obj.__age = -12
# print(obj)
# print(obj.__age)
# obj.set_age(-12)
obj.age = -234
print(obj)
print(obj.age)
# print(obj.get_age())
li = obj.skills
print(li)
li.append(123)
print(li)
print(obj.skills)
