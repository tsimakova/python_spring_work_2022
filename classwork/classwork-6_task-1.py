#todo: Написать функцию вычисления длины отрезка
'''
Условие
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
вычисляющую расстояние между точкой (x1,y1) и (x2,y2). Ввод значений считайте функцией input()
и выведите результат работы этой функции.

Примеры входа:
0
0
1
1

выходные данные:
1.41421
'''


def distance(x1, y1, x2, y2):
    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dis


x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))

res =  distance(x1, y1, x2, y2)
print(res)

