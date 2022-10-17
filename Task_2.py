# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

list_float = [1.99, 1.9, 3.1, 5, 10.01]
list_float = [round(i % 1, 2) for i in list_float]
result = max(list_float) - min(list_float)
print(result)