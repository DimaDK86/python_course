# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Введите число: ")
n = int(input())
p = 1
while p <= n:
    print(p, end=' ')
    p = p * 2