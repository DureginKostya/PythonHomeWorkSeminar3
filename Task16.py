'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1…N]. Пользователь в первой 
строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X
Пример:
5
    1 2 3 4 5
    3
    -> 1'''
from random import randint
try:
    number_range = int(input('Введите N: '))
    number = int(input('Введите X: '))
    if number_range > 0:
        user_array = [randint(-5, 5) for _ in range(number_range)]
        print(f'Массив: {user_array}')
        print(f'Число {number} встречается {user_array.count(number)} раз в массиве')
    else:
        print('Введено не допустимое значение')
except:
    print('Введено не допустимое значение')