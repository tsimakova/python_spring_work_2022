'''
#todo: Реализуйте функцию которая возвращает копию списка
def identity(nums):
    """Identity:
    Функция возвращает копию списка
    """
    pass
Пример вызова:
>>> identity([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
>>> identity([])
[]
'''

def identity(list):
    cp_list = list.copy()
    return cp_list

copied_list = identity([1, 2, 3, 4, 5])
print(copied_list)

'''
#todo: Реализуйте функцию которая возвращает степень числа каждого элемента
def power_(nums, pow):
    """Doubled:
    Функция возвращает степень каждого элемента
    """
    pass
Пример вызова:
>> > power_([1, 2, 3, 4, 5],2)
[2, 4, 6, 8, 10]
>> > power_([1, 2, 3, 4, 5],3)
[0, 3, 6, 9, 12, 15]
'''

def power(list, pow):
    return[i**pow for i in list]

powered_list = power([1, 2, 3, 4, 5], 3)
print(powered_list)

'''
#todo: Реализуйте функцию которая возвращает только четные значения
def evens(nums):
    """Evens:
      Функция возвращает четные значения каждого элемента
    """
    pass
Пример вызова:
>>> evens([1, 2, 3, 4, 5])
[2, 4]
>>> evens([1, 3, 5])
[]
>>> evens([-2, -4, -7])
[-2, -4]
'''

def evens(list):
    return[i for i in list if (i % 2) == 0]

even_list = evens([1, 2, 3, 4, 5])
print(even_list)

'''
#todo: Верните список с размерностью слов в том случае если они не исключение
# параметр exception принимает слово которое не нужно подсчитывать
def words_not_the(sentence, exception):
    """Words not 'the'
      Возвращает  список подсчинных слов без ислкючения (exception).
    """
    pass
Пример вызова:
>>> words_not_the('the quick brown fox jumps over the lazy dog', 'the' )
[5, 5, 3, 5, 4, 4, 3]
'''

def words_not_the(string, word):
    return[len(i) for i in string.split(' ') if i != my_word]

my_str = 'the quick brown fox'
my_word = 'the'

new_list = words_not_the(my_str, my_word)
print(new_list)

'''
#todo: Верните список гласных букв
def vowels(word):
    """Vowels:
        Функция возврашает список гласных букв
    """
    pass
>>> vowels('mathematics')
['a', 'e', 'a', 'i']
'''

def vowels(word):
    return[i for i in word if i in ('a', 'e', 'i', 'o', 'u')]

vowel_list = vowels('abban')
print(vowel_list)

'''
#todo: Задан массив [ 'one', 'two', 'three' ] с помощью спискового генератора преобразовать в словарь
# вида { 1:'one', 2:'two', 3:'three' }
'''

def list_to_dict_2(list):
    return[{(list.index(i) + 1): i} for i in list]

listed_dict = list_to_dict_2([ 'one', 'two', 'three' ])
print(listed_dict)