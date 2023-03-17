# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# n = [1, 1, 2, 0, -1, 3, 4, 4]
# print(set(n), type(set(n)))
# print(len(set(n)))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг -
# циклический) на K элементов вправо, K – положительное число.

# N = [1, 2, 3, 4, 5]
# K = int(input('Введите значение K: '))
#
# if K >= 0:
#     for i in range(K-1):
#         N.insert(0, N.pop())
# print(N)

# while K > 0:
#     N.append(N.pop())
#     K -= 1
#     print(N)

# Напишите программу для печати всех уникальных значений в словаре.

# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"},
#               {" VIII ": "S007"}]
#
# print(set(v for d in dictionary for v in d.values()))
#
# all_vals = set()
# for into_dict in dictionary:
#     val_set = set(into_dict.values())
#
#     all_vals |= val_set
#
# print(all_vals)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

arr_numbers = [0, -1, 5, 2, 3]
count = 0
for index in range(1, len(arr_numbers)):
    if arr_numbers[index] > arr_numbers[index - 1]:
        count += 1

print(len([arr_numbers[i] for i in range(1, len(arr_numbers)) if arr_numbers[i] > arr_numbers[i - 1]]))

