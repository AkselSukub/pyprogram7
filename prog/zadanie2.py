#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_sum_odd_indices(numbers):
    odd_indices_sum = sum(numbers[1::2])
    return odd_indices_sum

def calculate_sum_between_negatives(numbers):
    first_negative_index = -1
    last_negative_index = -1

    for i, num in enumerate(numbers):
        if num < 0:
            if first_negative_index == -1:
                first_negative_index = i
            last_negative_index = i

    if first_negative_index == -1 or last_negative_index == -1:
        return 0

    sum_between_negatives = sum(numbers[first_negative_index+1:last_negative_index])
    return sum_between_negatives

def compress_list(numbers):
    compressed_list = [num for num in numbers if abs(num) > 1]
    compressed_list.extend([0] * (len(numbers) - len(compressed_list)))
    return compressed_list

if __name__ == "__main__":
    numbers = [1.5, -2.3, 4.7, -3.2, 2.8, 0.9, -1.1, 5.2, -4.6]

    sum_odd_indices = calculate_sum_odd_indices(numbers)
    sum_between_negatives = calculate_sum_between_negatives(numbers)
    compressed_list = compress_list(numbers)

    print("Сумма элементов списка с нечетными номерами:", sum_odd_indices)
    print("Сумма элементов списка между первым и последним отрицательными элементами:", sum_between_negatives)
    print("Сжатый список:", compressed_list)