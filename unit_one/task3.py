# Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения с остатком.

x = float(input("Enter number "))
y = float(input("Enter number, except zero "))

print(x + y)  # Sum
print(x - y)  # Difference
print(x / y)  # Quotient
print(x * y)  # Multiplication
print(x // y)  # Division w/o remainder
print(x % y)  # Division with reminder
print(x ** y)  # Exponentiation
