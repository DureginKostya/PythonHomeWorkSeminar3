'''Задача 18: Требуется найти в массиве A[1…N] самый близкий по величине элемент к заданному числу X. Пользователь 
в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N 
целых чисел Ai. Последняя строка содержит число X
Пример:
5
    1 2 3 4 5
    6
    -> 5'''
from random import randint
try:
    number_range = int(input('Введите N: '))
    number = int(input('Введите X: '))
    if number_range > 0:
        user_array = [randint(-10, 10) for _ in range(number_range)]
        print(f'Массив: {user_array}')
        close_element = user_array[0]
        difference = abs(number - user_array[0])
        for i in range(1, number_range):
            if abs(user_array[i] - number) < difference:
                close_element = user_array[i]
                difference = abs(number - user_array[i])
        print(f'Самый близкий по величине элемент в массиве к числу {number} - {close_element}')
    else:
        print('Введено не допустимое значение')
except:
    print('Введено не допустимое значение')