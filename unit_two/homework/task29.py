#todo Задача 2. Транспонирование матрицы, transpose(matrix)
'''
Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
Пример:
>>> transpose([[1, 2, 3], [4, 5, 6]])
[[1, 4], [2, 5], [3, 6]]
||1 2 3||      ||1 4||
||4 5 6||  =>  ||2 5||
               ||3 6||
'''

mtx = [[1, 2, 3], [4, 5, 6]]

def transpose(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

tr_matrix = transpose(mtx)
print(tr_matrix)

