#:todo Релизовать функцию

'''
get_section(tuple_, elm)

На вход принимает кортеж и случайный элемент.  Нужно вернуть новый кортеж начинающийся
с первого вхождения элемента в исходный кортеж и заканчивающийся вторым его появлением.
Если искомого элемента нет – вернуть пустой кортеж. Если элемент найден только один раз,
то вернуть кортеж, с исходного элемента до конца.

'''

test_tuple = (4, 7, 7, 9, 12, 7, 2)
test_num = 12

def get_section(user_tuple, random_num):
    if random_num in user_tuple:
        X = user_tuple.index(random_num)
        if random_num in user_tuple[X + 1:len(user_tuple)]:
            Y = (user_tuple[X + 1:len(user_tuple)]).index(random_num)
            new_tuple = (X, Y + X + 1)
            return(new_tuple)
        else:
            new_tuple = (X, )
            return(new_tuple)
    else:
        empty_tuple = ()
        return(empty_tuple)


result = get_section(test_tuple, test_num)
print(result)








