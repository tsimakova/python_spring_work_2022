#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
'''
Содержимое файла import_this.txt
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

выходные данные
Complex is better than complicated.
Simple is better than complex.
Explicit is better than implicit.
Beautiful is better than ugly.

'''

fd = open('D:\python_homework\import_this.txt', 'r+', encoding = 'utf-8')

forward_list = fd.readlines()

reverse_list = forward_list[::-1]

fd.write('\n')

for el in reverse_list:
    fd.write(el)

fd.close