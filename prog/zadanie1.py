#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Оценки по алгебре, геометрии и физике соответственно
grades_algebra = [5, 4, 3, 4, 5, 2, 4, 5, 4, 3]
grades_geometry = [4, 5, 3, 4, 2, 5, 4, 3, 4, 5]
grades_physics = [3, 4, 5, 3, 4, 5, 2, 4, 5, 4]

# Функция для определения средней оценки по предмету
def average_grade(grades):
    return sum(grades) / len(grades) if len(grades) > 0 else 0

# Функция для определения количества учащихся без двоек
def students_without_twos(grades):
    return len([grade for grade in grades if grade != 2])

# Определение средней оценки по алгебре с использованием цикла
average_algebra_loop = average_grade(grades_algebra)
print(f'Средняя оценка по алгебре (цикл): {average_algebra_loop:.2f}')

# Определение количества учащихся без двоек по алгебре с использованием цикла
students_without_twos_algebra_loop = students_without_twos(grades_algebra)
print(f'Количество учащихся без двоек по алгебре (цикл): {students_without_twos_algebra_loop}')

# Определение средней оценки по алгебре с использованием List Comprehensions
average_algebra_comprehension = average_grade([grade for grade in grades_algebra])
print(f'Средняя оценка по алгебре (List Comprehensions): {average_algebra_comprehension:.2f}')

# Определение количества учащихся без двоек по алгебре с использованием List Comprehensions
students_without_twos_algebra_comprehension = len([grade for grade in grades_algebra if grade != 2])
print(f'Количество учащихся без двоек по алгебре (List Comprehensions): {students_without_twos_algebra_comprehension}')