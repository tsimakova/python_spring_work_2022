# :todo Написать функцию is_ascending(list_) проверки на монотонность?
'''

Функция принимает список и определяет  является ли он монотонно возрастающим
(то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

Пример:
mass = [ 2, 5, 7]

def is_ascending(list_):
    ваша реализация


result = is_ascending(mass)
print(result)
YES

'''

def is_ascending(user_list):
    ascending_values = []  # create list for values comparing result
    for index in range(len(user_list) - 1):
        if user_list[index] < user_list[index + 1]:  # compare index value and next index value
            ascending_values.append("YES")
        else:
            ascending_values.append("NO")
    if "NO" in ascending_values:  # check results if ascending order is broken
        print("NO")
    else:
        print("YES")



mass = [2, 3, 7]

is_ascending(mass)



