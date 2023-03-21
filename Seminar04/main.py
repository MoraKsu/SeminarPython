import random

# Задача №25. Решение в группах Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# Решение срезами
"""
arr = "a a a b c a a d c d d".split(" ")
result_arr = []

for index_chr in range(len(arr) - 1):
    count = arr[:index_chr].count(arr[index_chr])
    result_arr.append(f"{arr[index_chr]}_{count}" if count > 0 else f"{arr[index_chr]}")
print(" ".join(result_arr))

# Решение через словарь

my_input = input('Введите строку--> ').split()
my_result = []
my_dict = dict()
for i in my_input:
    my_result.append(i)
    if i in my_dict:
        my_result.append('_' + str(my_dict[i]))
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(*my_result)

# Еще одно решение через словарь

s = ("a a a b c a a d c d d").split()
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 0
        print(i, end=' ')
    elif i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
"""
# Задача №27. Решение в группах Пользователь вводит текст(строка). Словом считается последовательность непробельных
# символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm
# sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# my_str = "She      sells sea     shells on the " \
# "sea shore The shells that she sells are sea shells "\
# "I'm sure So if she sells sea shells on the sea shore "\
# "I'm sure that the shells are sea shore shells"
#
# print((set(my_str.split())))

# Задача №29. Решение в группах Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2 друга оказались
# не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше
# ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# Первое решение

# numb = int(input('-->'))
# max_number = numb
# while numb != 0:
#    numb = int(input('-->'))
#    if max_number < numb:
#       max_number = numb
# print(max_number)

# Второе решение через рандом

subsequence = [random.randint(0, 100) for i in range(int(input('count: ')))]
print(subsequence)
print(max(subsequence) if (0 in subsequence) == False else max(subsequence[:subsequence.index(0)]))

