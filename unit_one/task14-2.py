# todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.
"""
Пример:
mass = [1,2,17,16,30,51,2,70,3,2]
Для числа 2 индексы двух ближайших чисел: 6 и 9
Пример:
mass = [1,2,17,54,30,89,2,1,6,2]
Для числа 1 индексы двух ближайших чисел: 0 и 7
Для числа 2 индексы двух ближайших чисел: 6 и 9
"""


lst = [1, 2, 17, 54, 30, 89, 2, 1, 6, 0]




'''
lst = [1, 2, 17, 54, 30, 89, 2, 1, 6, 0]
u_input = int(input("Enter number "))
difs = []

for i in lst:
    difs.append(abs(i - u_input))  # create list of differences

print(lst)

first = difs.index(min(difs))  # find index of fisrt minimal value (difference)

difs[int(difs.index(min(difs)))] = (max(difs))  # chgange founded first minimal value to maximum value

second = difs.index(min(difs))  # find index of second minimal value (difference)

if first > second:  # sort first and second indexes in numerical order and print output
    print("For number " + str(u_input) + " nearest indexes are: " + str(second) + " and " + str(first))
else:
    print("For number " + str(u_input) + " nearest indexes are: " + str(first) + " and " + str(second))

'''


