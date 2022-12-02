a = 4
b = 9
if a > b:
    print('Код выполняемый если выражение истина')
else:
    print('Код выполняемый если выражение ложь')

variable = int(input("Введите число: "))
if '3' in str(variable):
    print('Здесь пахнет тройкой')

if variable % 2 == 0:
    print('четное')
else:
    print("нечетное")

# попадает ли число в диапазон от 3 до 19
if 3 < variable < 19:
    print("в диапазоне")
else:
    print("за пределами")

# попадает ли число в диапазон от 6 до 356 и при этом содержит 7 и 3
if 6 < variable < 356 and '7' in str(variable) and '3' in str(variable):
    print('Все совпало')
else:
    print("чего-то не хватает")

# попадает ли число в диапазон 1 - 4 или 10 - 14
if 1 < variable < 4 or 10 < variable < 14:
    print('попал')
else:
    print("мимо")

# определить сумму покупки в зависимости от скидки
# до 500 грн - без скидки
# от 500 до 1000 - 5%
# от 1000 - 8%
price = float(input('Введите сумму покупки: '))
if price < 500:
    print(f'К оплате {price}')
elif price < 1000:
    print(f'К оплате {price * 0.95}')
else:
    print(f'К оплате {price * 0.92}')
print(
    '''
    Играть - нажмите 1
    Опции - Нажмите 2
    Загрузить - нажмите 3
    Сохранить - нажмите 4
    Выход - нажмите любую клавишу
    '''
)
user_choice = input('Сделайте ваш выбор: ')
if user_choice == '1':
    print('Play piano')
elif user_choice == '2':
    pass
elif user_choice == '3':
    print('Грузимся')
elif user_choice == '4':
    print('Храним')
elif user_choice == 'godmode':
    print('Включил читы...')
else:
    print('Прощаемся')

describe = input('опишите: ')

if 'скользкий' in describe:
    print('фу')
if 'пушистый' in describe:
    print('погладить')
if 'грязный' in describe:
    print('помыть')
if 'мягкий' in describe:
    print('спрятать')
if 'твердый' in describe:
    print('выбросить')
