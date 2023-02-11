# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n = int(input("Enter the number of elements of the 1st set: "))
m = int(input("Enter the number of elements of the 2nd set: "))
a = [0] * n
b = [0] * m
for i in range(n):
    a[i] = int(input(f"Enter {i+1} element of 1st set: " ))
for i in range(m):
    b[i] = int(input(f"Enter {i+1} element of 2nd set: " ))
c = a + b
c.sort()
d = set(c)
for d in d:
    print (d, end = " ")

