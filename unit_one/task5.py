# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

A = float(input("Enter A (A>0) "))
B = float(input("Enter B (B>A) "))
C = float(input("Enter C (C>B) "))

print("AC = " + str(C - A))
print("BC = " + str(C - B))
print("Sum = " + str((C - A) + (C - B)))