from math import sqrt

# Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1,
# ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fibonacci(n):
#     if n in (0, 1):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = int(input("--> "))
# print(fibonacci(n))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# mark_to_replace = int(input("Оценка, на которую нужно заменить: "))
# marks = input("Оценки ученика через пробел: ").split()
# marks = [int(mark) for mark in marks]
#
# for i in range(len(marks)):
#     if marks[i] == max(marks) and max(marks) == mark_to_replace:
#         marks[i] = min(marks)
#     elif marks[i] == max(marks):
#         marks[i] = min(marks)
#     elif marks[i] == mark_to_replace:
#         marks[i] = max(marks)
#
# print(*marks)

# Второе решение

# N = int(input("Оценка, на которую нужно заменить: "))
# arr = list(map(int, input("Оценки ученика через пробел: ").split(maxsplit=N)))
#
# min = 1000
# max = 0
# for i in range(len(arr)):
#     if arr[i] < min:
#         min = arr[i]
#     if arr[i] > max:
#         max = arr[i]
#
# for i in range(len(arr)):
#     if arr[i] == max:
#         arr[i] = min
#
# for i in range(len(arr)):
#     print(arr[i], end=' ')

# Третье решение:

# list1 = [1, 3, 3, 3, 4]
#
#
# def find_min_max(list):
#     min = max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#         elif i < min:
#             min = i
#     return min, max
#
#
# def replace(list, min, max):
#     for i in range(len(list)):
#         if list[i] == max:
#             list[i] = min
#     return list
#
#
# (a, b) = find_min_max(list1)
# print(replace(list1, a, b))

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание: Простое число -
# это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def is_prime(n):
#     i = 2
#     while i <= sqrt(n):
#         if n % i == 0:
#             return False
#         i += 1
#     if n > 1:
#         return True
#
#
# a = int(input("Введите число для проверки: "))
#
# if is_prime(a):
#     print("Yes")
# else:
#     print("No")

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном
# порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:  2 -> 3 4
# Output: 4 3

# def reverse_sequence(n):
#     if n == 0:
#         return
#     x = input("Введите элемент: ")
#     reverse_sequence(n - 1)
#     print(x, end=" ")
#
#
# n = int(input("Введите количество элементов: "))
# reverse_sequence(n)
