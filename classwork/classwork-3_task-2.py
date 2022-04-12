# todo: Задано целое число от 10 до 99 , нобходимо найти сумму и произведение его цифр

# Пример:
# x = 23     →   2 + 3
# Ответ:
# сумма - 5
# произведение - 6

x = str(input("Enter number from 10 to 99 "))

print("Sum = "+ str(int(x[0]) + int(x[-1])))

print("Multiplication = "+ str(int(x[0]) * int(x[-1])))
