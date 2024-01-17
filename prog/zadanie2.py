#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Исходный список вещественных элементов
original_list = [4.5, -2.0, 1.2, -3.8, 2.7, 5.1, -1.5, 3.3]

# Переупорядочивание элементов массива: сортировка по возрастанию
sorted_list = sorted(original_list)

# Вычисление суммы элементов списка с нечетными номерами
sum_odd_indices = sum(sorted_list[1::2])

# Находим индексы первого и последнего отрицательных элементов
first_negative_index = sorted_list.index(next(x for x in sorted_list if x < 0))
last_negative_index = sorted_list.index(next(x for x in reversed(sorted_list) if x < 0))

# Вычисление суммы элементов списка между первым и последним отрицательными элементами
sum_between_negatives = sum(sorted_list[first_negative_index+1:last_negative_index])

# Вывод результатов
print(f'Исходный список: {original_list}')
print(f'Переупорядоченный список: {sorted_list}')
print(f'Сумма элементов с нечетными номерами: {sum_odd_indices}')
print(f'Сумма элементов между первым и последним отрицательными: {sum_between_negatives}')