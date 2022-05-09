
import random



a = input("Please select an option:\n"
          "1. Start a new game.\n"
          "2. Load the game.")

if int(a) == 1:
    print("one")
elif int(a) == 2:
    print("two")
else:
    print("three")


'''
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


'''

