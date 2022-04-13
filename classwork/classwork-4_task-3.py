# todo: Написать игру , где программа загадывает число от 0 до 100 (через функцию random) , а пользователь
# пытается его отгадать(через консоль). При успехе выводится поздравление в победе и результат попыток.
# По истечении 10 неудачных попыток выводится проигрышь.

# Для получения функции числа из диапазона от 0 до 100 подключать библиотеку
# import random
# random.randint(0,100)

import random

x = random.randint(0,100)
print(x)

y = int(input("Enter integer "))
attempt = []
count = 1


while count < 10:
    if y == x:
        print("Congratulations!")
        print("Counts = " + str(count))
        break
    if y != x:
        count = count + 1
        attempt.append(count)
        y = int(input("Incorrect, try again. Enter integer "))
        continue
else:
    print("Failure!")




