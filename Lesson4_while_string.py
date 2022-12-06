'''
while выражение:
    тело цикла
'''
# password = '123'
# pass_in = input('Введите пароль: ')
# while pass_in != password:
#     print('Неверно!')
#     pass_in = input('Попробуйте еще: ')
# print('Ура, получилось')

# password = '123'
# while True:
#     pass_in = input('Input password: ')
#     if pass_in == password:
#         break  # прерывает выполнение цикла
#     print('Wrong pass!')
# print('Ура')

# num = int(input('Input number: '))
# result = 0
# while num > 0:
#     result += num % 10  # result = result + num % 10
#     num = num // 10
# print(result)
#
# num2 = int(input('Input number: '))
# result = 0
# while num2 > 0:
#     result = result * 10 + num2 % 10
#     num2 = num2 // 10
# print(result)

for h in range(5):
    for w in range(5):
        print('*', end=' ')
    print()
print()
for h in range(5):
    for w in range(h+1):
        print('*', end=' ')
    print()
print()
for h in range(5, 0, -1):
    for w in range(h ):
        print('*', end=' ')
    print()
