"""
Decorators - функціі які у якості параметра приймають функцію,
 та повертають в якості результатат теж функцію
"""


def decor(some_fun):
    def inner_fun(li: list):
        result = some_fun(li)
        if result < 0: result = 0
        return result

    return inner_fun


@decor
def my_sum(li: list):
    return sum(li)


li = [1, -2, -3, 4, -5]
print(my_sum(li))


def pretty_text(fun_printing_text):
    def output():
        print('*' * 10)
        fun_printing_text()
        print('*' * 10)
    return output

@pretty_text
def print_hello():
    print('Hello')

print_hello()