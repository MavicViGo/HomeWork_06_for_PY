'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного максимума)
'''

list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(list1)
min_el = int(input('введите индекс минимального эл-та: '))
max_el = int(input('введите индекс максимального эл-та: '))
for i in range(len(list1)):
    j = 0
    if min_el<list1[i]<max_el:
        print(i, end=', ')