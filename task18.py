# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input('Введите колличество элементов: '))
a = [int(input('Введите числа: ')) for i in range(n)]
x = int(input('Введите искомое число: '))

if a[0]>=x:
    if a[0] == x:
        print(f'Число {a[0]} равно {x}')
    else:
        max_for_x = a[0]
        min = x
        min_for_x = 0
        for i in range(n-1):
            if a[i+1] == x:
                print(f'Число {a[i+1]} равно {x}')
            else:
                if a[i+1]>x and a[i+1]< max_for_x:
                    max_for_x = a[i+1]
                else:
                    if a[i+1]<x and a[i+1] < min:
                        min = a[i+1]
                    elif a[i+1]<x and a[i+1] > min:
                        min_for_x = a[i+1] 
        if ((x - min) == ( max_for_x -x )):
            print(f'Числа{min_for_x, max_for_x} ближе всех к {x}')
        else:
            print(f'Число {min_for_x} ближе всех к {x}' if (min_for_x != 0) and (x- min_for_x) < ( max_for_x -x ) else f'Число {max_for_x} ближе всех к {x}')

else:
    min_for_x = a[0]
    max = 0
    max_for_x = x
    for i in range(n-1):
        if a[i+1] == x:
            print(f'Число {a[i+1]} равно {x}')
        else:
            if a[i+1]<x and a[i+1]> min_for_x:
                min_for_x = a[i+1]
            elif a[i+1] > x and max_for_x == x:
                max = max_for_x = a[i+1]
            elif a[i+1]>x and a[i+1]> max:
                max = a[i+1]
            elif a[i+1]>x and a[i+1]<max_for_x:
                max_for_x = a[i+1]
    print(min_for_x)
    print(max)
    print(max_for_x)
    if ((max_for_x - x) == (x - min_for_x)):
        print(f'Числа{min_for_x, max_for_x} ближе всех к {x}')
    else:
        print(f'Число {max_for_x} ближе всех к {x}' if (max_for_x !=0) and (max_for_x - x) < (x - min_for_x) else f'Число {min_for_x} ближе всех к {x}')




