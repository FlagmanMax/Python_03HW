# Task 02
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import math

def inputList(n):
    lst1 = []
    for i in range(n):
        lst1.append(random.randint(0,n))
    return lst1

def MakeListPairsProduction(lst1):
    lst2 = []
    for i in range((math.ceil(len(lst1)/2))):
        lst2.append(lst1[i]*lst1[len(lst1)-1-i])
        #* lst1[len(lst1)-i-1]
    return lst2

n = int(input("Введите длину списка "))

lst1 = inputList(n)
print(f"исходный список:\t\t {lst1}")

lst2 = MakeListPairsProduction(lst1)
print(f"список из произведений пар:\t {lst2}")