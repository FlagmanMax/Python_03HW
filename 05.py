# Task 05
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n == 0:
        return 0
    elif n in (1, -1):
        return 1
    if (n > 0):
        return fib(n-1)+fib(n-2)
    else:
        return fib(n+2) - fib(n+1)

lst1 = []
k = int(input("Введите число "))
for i in range(k+1):
    lst1.append(fib(i))
    if i != 0:
        lst1.insert(0,fib(-i))
print(lst1)    