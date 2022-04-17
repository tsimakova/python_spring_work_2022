#todo 3.1: Получите заданное количество N (например, 20) различных
# случайных целых чисел в диапазоне от 0 до N-1. Найдите их
# сумму.


#todo 3.2:  Известно, что сейф открывается при правильном вводе
# кода из 3 цифр 0...9. Задайте код и затем откройте сейф, ис-
# пользуя метод перебора с помощью нескольких операторов
# цикла for.

import random  # Import library for random numbers generation.

# task 3.1

N = int(input("Enter list length "))  # Define how many random numbers should be listed.
random_list = []
count = 0

while count < int(N):  # Create list of random numbers of certain length.
    random_list.append(int(random.randint(0, int(N))))
    count = count + 1

print(random_list)

total = 0

for i in random_list:
    total = total + i

print(total)

# task 3.2

X = int(input("Enter code length "))
code_list = []
result = []
count = 0

while count < X:
    code_list.append(int(random.randint(0, 9)))
    count = count + 1

print(code_list)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in code_list:
    for j in numbers:
        if j == i:
            result.append(j)
print(result)
