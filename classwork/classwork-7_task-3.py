#todo: Модифицировать программу таким образом чтобы она выводила при повторном считывании стр. 5 приветствие "Hello"

f = open("D:\\PYTHON_course\\text.txt", "r+")  # open file for reading and writing
f.write("Hello\n")  # save string to the opened file
print(f.read(5))  # read first 5 bytes of the file

f.close()

'''
Hint!!!

with open('D:\\PYTHON_course\\text.txt', 'r+') as f:
    f.write('0123456789abcdef')
    print(f.seek(5))  # Перемещаемся к 6-му байту от начала файла.
    print(f.read(3))  # '5'
    f.seek(-3, 2)  # Перемещаемся к третьему байту от конца файла.
    f.read(1)  # 'd'

'''