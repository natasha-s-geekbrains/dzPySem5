# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

a = int(input("Введите первое целое неотрицательное число: "))
b = int(input("Введите второе целое неотрицательное число: "))

def sum(x, y):
    if y == 0:
        return x
    else:
        x+=1
        y-=1
    return sum(x, y)

print(sum(a, b))
