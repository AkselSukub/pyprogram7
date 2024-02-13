#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_average_grade(grades):
    total_sum = sum(grades)
    average_grade = total_sum / len(grades)
    return average_grade

def count_students_without_twos(grades):
    count = 0
    for grade in grades:
        if grade != 2:
            count += 1
    return count

if __name__ == "__main__":
    A = [4, 5, 3, 4, 5]
    G = [3, 2, 4, 5, 3]
    F = [5, 5, 4, 2, 5]

    average_algebra_grade = calculate_average_grade(A)
    students_without_twos = count_students_without_twos(A)

    print("Средняя оценка по алгебре:", average_algebra_grade)
    print("Количество учащихся без двоек:", students_without_twos)