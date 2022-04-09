# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

A = int(input("Enter integer A "))
B = int(input("Enter integer B "))
C = int(input("Enter integer C "))

A = A + B + C 
B = A - B - C
C = A - B - C
A = A - B - C

print("A = " + str(A))
print("B = " + str(B))
print("C = " + str(C))
