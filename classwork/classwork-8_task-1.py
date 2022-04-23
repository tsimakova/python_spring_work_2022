#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
'''
#Формат вывода:
Количество букв a - 13
Количество букв o - 12
Количество букв e - 11
.....................
'''

fd = open('D:\PYTHON_course\dump.txt', 'r', encoding='utf-8')
text = fd.read()
vowel = ['а', 'у', 'о', 'и', 'э', 'ы']
count_list = []

for i in vowel:
    if

    if vowel[0] == i:
            a_count = a_count + 1
    if vowel[1] == i:
            y_count = y_count + 1
    if vowel[2] == i:
            o_count = o_count + 1
    if vowel[3] == i:
            i_count = i_count + 1
    if vowel[4] == i:
            e_count = e_count + 1
    if vowel[5] == i:
            x_count = x_count + 1

print('Количество букв a - ' + str(a_count))
print('Количество букв у - ' + str(y_count))
print('Количество букв о - ' + str(o_count))
print('Количество букв и - ' + str(i_count))
print('Количество букв э - ' + str(e_count))
print('Количество букв ы - ' + str(x_count))

