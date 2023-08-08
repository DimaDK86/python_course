# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import os
os.system('cls' if os.name == 'nt' else 'clear')

import random

array = [random.randint(-20, 20) for i in range(random.randint(5, 10))]

print(*array)

min = int(input("Ведите минимальное значнение: "))
max = int(input("Ведите максимальное значнение: "))

array2 = []

if max >= min:

   for i in range(len(array)):

      if max >= array[i] and min <= array[i]:

          array2.append(i)

   print("Элемментов в диапозоне:",len(array2))

   print("Индексы элементов:",array2)




