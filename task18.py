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
flag =True
for i in range (n):
    if a[i]==x:
        flag = False
if flag == False:
    print('Число есть в массиве')
else:
    if a[0]>x:
    
        max_to_x = a[0]
        min_to_x = x
        for i in range(n-1):
            if a[i+1]>x and a[i+1]< max_to_x:
                max_to_x = a[i+1]
            else:
                if a[i+1]<x and  min_to_x==x:
                    min_to_x = a[i+1]
                elif a[i+1]<x and a[i+1]>min_to_x:
                    min_to_x = a[i+1]
        if ((x - min_to_x) == ( max_to_x -x )):
            print(f'Числа{min_to_x, max_to_x} ближе всех к {x}')
        else:
            print(f'Число {min_to_x} ближе всех к {x}' if (min_to_x != x) and (x- min_to_x) < ( max_to_x -x ) else f'Число {max_to_x} ближе всех к {x}')

    else:
        min_to_x = a[0]
        max = 0
        max_to_x = x
        for i in range(n-1):
        
            if a[i+1]<x and a[i+1]> min_to_x:
                min_to_x = a[i+1]
            elif a[i+1] > x and max_to_x == x:
                max = max_to_x = a[i+1]
            elif a[i+1]>x and a[i+1]> max:
                max = a[i+1]
            elif a[i+1]>x and a[i+1]<max_to_x:
                max_to_x = a[i+1]
        if min_to_x>max:
            print(f'Число {min_to_x} ближе всех к {x}')
        elif ((max_to_x - x) == (x - min_to_x)):
            print(f'Числа{min_to_x, max_to_x} ближе всех к {x}')
        else:
            print(f'Число {max_to_x} ближе всех к {x}' if (max_to_x !=0) and (max_to_x - x) < (x - min_to_x) else f'Число {min_to_x} ближе всех к {x}')




