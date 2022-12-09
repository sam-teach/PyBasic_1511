# проверка, является ли число простым
number = int(input('Input number: '))
for i in range(2, number // 2 + 1):
    if number % i == 0:
        print('Число не простое')
        break
else:
    # этот блок выполнится только если цикл завершился сам,
    # без прерывания(break)
    print('число простое')
