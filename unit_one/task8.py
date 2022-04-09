# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

A = int(input("Enter integer A "))
B = int(input("Enter integer B "))
C = int(input("Enter integer C "))

A = A + B + C  # 12, 4, 5
B = A - B - C  # 12, 3, 5
C = A - B - C  # 12, 3, 4
A = A - B - C  # 5, 3, 4

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))