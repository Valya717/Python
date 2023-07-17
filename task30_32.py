# # Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# # разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# # an = a1 + (n-1) * d.
# # Каждое число вводится с новой строки.

# start = int(input('Введите первый элемент: '))
# step = int(input('Введите разность элементов: '))
# n = int(input('Введите кол-во элементов: '))

# def progreshion(start,step,n):
#     list_res = []
#     for i in range(n):
#         list_res.append(start + i*step)
#     print(list_res)
# result = progreshion(start, step,n)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
def generate_list(len_list):
    list_res = []
    for i in range(len_list):
        list_res.append(random.randint(-20, 20))
    return list_res
min = int(input('Введите минимум диапозона: '))
max = int(input('Введите максимум диапозона: '))
n = int(input('Введите длину массива: '))
massiv = generate_list(n)
result = []
for i in range(n):
    if min < massiv[i]< max:
        result.append(i)
print(massiv)
print(result)