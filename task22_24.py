
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

# def generate_list(len_list):
#     list_res = []
#     for i in range(len_list):
#         list_res.append(random.randint(1, 20))
#     return list_res

# n = int(input('Введите сколько элементов в первом списке: '))
# m = int(input('Введите сколько элементов во втором списке: '))
# list_1 = generate_list(n) 
# list_1 = set(list_1)
# list_2 = generate_list(m)
# list_2 = set(list_2)

# list_3 = list_1.union(list_2)

# print(list_1)
# print(list_2)
# print(list_3)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

def generate_list(len_list):
    list_res = []
    for i in range(len_list):
        list_res.append(random.randint(1, 20))
    return list_res
n = int(input('Введите количество кустов: '))
data = generate_list(n)
max = 0
for i in range (n):
    if i < n-2:
        result = data[i]+data[i+1]+data[i+2]
    elif i == n-2:
        result  = data[i]+data[i+1]+data[0]
    elif i == n-1:
        result  = data[i]+data[0]+data[1]
    if result > max:
        max = result
    print(result)

print (data)
print (max)
    