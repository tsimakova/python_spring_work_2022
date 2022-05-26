#todo: Найти сумму элементов матрицы,
'''
Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> msum(matrix)
21

>>> msum(load_matrix('matrix.txt'))
423
'''

mtx = [[1, 2, 3], [4, 5, 6]]

def msum(matrix):
    row_sum = []
    for i in matrix:
        row_sum.append(sum(i))
    return sum(row_sum)

mtx_sum = msum(mtx)
print(mtx_sum)