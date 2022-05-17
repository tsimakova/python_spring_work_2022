#todo: I вариант (алгоритм сортировки вставками)
'''
Реализовать на Python алгоритм сортировки вставками представленный в псевдокоде
в учебнике “Introduction to Algorithms”  на стр. 57 - 63.

Задача.
Перепишите процедуру INSERTION_SORT и отсортируйте последовательность
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7] по убыванию.
'''

#A = [5, 3, 2, 1, 4]
A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]

print(A)

'''
The insertion_sort function sort the values of the list in the ascending order using the insertion algorithm.

'''

def insertion_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return(list)

insertion_sort(A)
print(A)