#todo: Задан файл dictionary.xml (в текущей папке).
'''
<dict>
    <key>###</key>
    <value>##</value>
</dict>

Написать функцию которая принимает кортеж вида  ('age', 16) и записывает его значения в файл
Первое значение кортежа в позицию <key> второе в <value>
Итоговый файл должен получиться:
<dict>
<key>'age'</key>
<value>16</value>
</dict>

Задачу решить с помощь метода seek()
'''

my_tuple = ('age', 16)

def fill_xml(values):  # fill in xml file with values from the tuple
    f = open("D:\\PYTHON_course\\dictionary.xml", "r+")  # open file for reading and writing
    f.seek(17)  # move coursor to the 17th byte from the beginning of the file
    f.write(my_tuple[0])  # save first value from the tuple to the opened file
    f.seek(39)  # move coursor to the 39th byte from the beginning of the file
    f.write(str(my_tuple[1]))  # save second value from the tuple to the opened file
    f.close

fill_xml(my_tuple)