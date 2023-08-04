# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import os
os.system('cls' if os.name == 'nt' else 'clear')


n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    num = int(input())
    set1.add(num)

print("Введите элементы второго множества:")
for i in range(m):
    num = int(input())
    set2.add(num)

elements = set1.intersection(set2)
sortelements = sorted(elements)

print("Общие элементы в порядке возрастания:")
for num in sortelements:
    print(num)