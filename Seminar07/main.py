from math import *


# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество
# раз и вы не хотите ничего сломать): transformation = <???> values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# или любой другой список transformed_values = list(map(transformation, values)) Единственный способ вашего
# взаимодействия с этим кодом - посредством задания функции transformation. Однако вы поняли, что для вашей текущей
# задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть. Напишите такое
# лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Ввод:
# transformation = lambda item: item
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
# Вывод: ok

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию f ind_farthest_orbit(list_of_orbits), которая среди списка орбит планет
# найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен
# быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя
# кортеж из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в
# два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь.
# Гарантируется, что самая далекая планета ровно одна
# Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#       print(*find_farthest_orbit(orbits))
# Вывод: 2.5 10

# Первое решение

# def find(orbits):
#     orbits = [(a, b) for (a, b) in orbits if a != b]
#     space = [a * b for (a, b) in orbits]
#     return (orbits[space.index(max(space))])
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find(orbits))

# Второе решение

# def find_farthest_orbit(list_of_orbits: list[tuple]) -> tuple:
#     max_square = 0
#     max_square_index = 0
#     for i in range(len(list_of_orbits)):
#         orbit = list_of_orbits[i]
#         orbit_x: int = orbit[0]
#         orbit_y: int = orbit[1]
#         if orbit_x == orbit_y: continue
#         square = pi * (orbit_x * orbit_y)
#         if max_square > square: continue
#         max_square_index = i
#         max_square = square
#     return list_of_orbits[max_square_index]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Третье решение

# def find_farthest_orbit(orbits):
#     return max({a * b: (a, b) for a, b in orbits if a != b}.items())
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits)[1])

# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его характеристику.
# Ввод:
def same_by(func, vals):
    return True if len(set(map(func, vals))) <= 1 else False


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
# Вывод: same
