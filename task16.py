'''Задача 16:
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X.
'''
n = int(input('Введите колличество элементов: '))
a = [int(input('Введите числа: ')) for i in range(n)]
x = int(input('Введите искомое число:'))
count = 0
for i in range(n):
    if a[i] == x:
        count +=1
# print(f'Число {x} встерчается {count} раз')
print(f"Число {x} не встречается" if count == 0 else f'Число {x} встерчается {count} раз')



# import typing


# numbers = [int(input()) for _ in range(int(input('Enter a number: ')))]
# X = int(input("Введите искомое число:"))

# result = numbers.count(X)

# print(f'The number {X} occurs in numbers {result} times.')
# print(f'Numbers list: {numbers}.')