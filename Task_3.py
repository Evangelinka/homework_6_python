# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from functools import reduce

my_list = [123, 34, 3, 56, 10, 20, 57, 69, 7331]
sum_list = reduce(lambda x, y: x + y, map(lambda x: x[0], filter(lambda x: x[1] % 2 == 0, zip(my_list, range(1, len(my_list) + 1)))))
print(sum_list)