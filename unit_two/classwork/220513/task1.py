#todo Задача 1. Чтение матрицы, load_matrix(filename)
# Дан файл, содержащий таблицу целых чисел вида
'''
(в каждой строке через пробел записаны числа)

11 12 13 14 15 16
21 22 23 24 25 26
31 32 33 34 35 36

Т.е. в каждой строке через пробел записаны числа.
Требуется написать функцию load_matrix(filename) которая загружает эту таблицу из файла.
Если в каждой строке находится одинаковое количество чисел, функция возвращает список списков целых чисел.
В противном случае возвращает False.

Задачу следует решить с использованием списковых включений, циклы использовать НЕЛЬЗЯ!
'''

#mx_file = open('D:\PYTHON_course\matrix.txt', 'r')
mx_file = open('D:\PYTHON_course\matrix2.txt', 'r')

mx_list = []
mx_list = [str(str(line).split('\n')[0]).split(' ') for line in mx_file]

mx_bool = ''
mx_bool = [(mx_bool + 'True') if len(mx_list[i-1]) == len(mx_list[i]) else (mx_bool + 'False') for i in range(len(mx_list))]

final = 'False' if 'False' in mx_bool else mx_list
print(final)

