'''
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.
A
            *
          *   *
        *       *
      *           *
    *               *
  *                   *
* * * * * * * * * * * * *
1 1
2 3
3 5
4 7
5 9
6 11
7 13

'''

h = 7

for string_ in range(1, h + 1):
    for space_ in range(0, h * 2 - string_ * 2):
        print('-', end='')
    for star in range(string_ + (string_ - 1)):
        if star == 0 or star == string_ + (string_ - 1) - 1 or string_ == h:
            print('*', end=' ')
        else:
            print('-', end=' ')
    print()
