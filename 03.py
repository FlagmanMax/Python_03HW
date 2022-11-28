# Task 03
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def inputList(n):
    lst1 = []
    for i in range(n):
        lst1.append(float(random.randint(0,1000)/100))
    return lst1

def makeFracList(lst1):
    lst2 = []
    for i in range(len(lst1)):
        lst2.append(round(lst1[i] - int(lst1[i]),2))
    return lst2


n = int(input("Введите длину списка "))

lst1 = inputList(n)
print(f"исходный список:\t\t {lst1}")

lst2 = makeFracList(lst1)
print(f"список дробных частей:\t\t {lst2}")

lst2.sort()
print(f"отсортированный список:\t\t {lst2}")

result = lst2[n-1] - lst2[0]
print(f"разность максимальной и минимальной дробных частей = \t {result}")