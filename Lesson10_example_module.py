num = 1234


def fun():
    """
    fun hello
    :return: null
    """
    print('hello')


def calc(num1, op: str, num2):
    """
    небезопасный калькулятор
    :param num1:
    :param op:
    :param num2:
    :return: результат операции
    """
    return eval(f'{num1}{op}{num2}')
