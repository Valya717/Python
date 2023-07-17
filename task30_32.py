# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

start = int(input('Введите первый элемент: '))
step = int(input('Введите разность элементов: '))
n = int(input('Введите кол-во элементов: '))

def progreshion(start,step,n):
    list_res = []
    for i in range(n):
        list_res.append(start + i*step)
    print(list_res)
result = progreshion(start, step,n)