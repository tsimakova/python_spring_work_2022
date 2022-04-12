# todo: Задана поизвольная строка. Необходимо разбить ее на две части.
# Задачу решить с помощью срезов.
#
# Пример:
# str = "Hello world!"
# Ответ: Первая часть  "Hello"
# 		Вторая часть "world!"


string = str(input("Type sting: "))

print("Left part:" + "\"" + str(string[0:int(len(string)/2)]) + "\"")
print("Right part:" + "\"" + str(string[int(len(string)/2):]) + "\"")
