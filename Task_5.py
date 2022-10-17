# Дан список из 15 случайных чисел. Переписать его элементы в новый список
# следующим образом: сначала все нечетные, затем все четные. И отсортировать.

import random

my_list = [random.randint(1, 9) for i in range(15)]
result = sorted([i for i in my_list if i % 2 == 1]) + sorted([i for i in my_list if i % 2 == 0])
print(my_list)
print(result)