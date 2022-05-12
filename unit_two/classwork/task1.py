#todo: Реализовать декоратор который подсчитывает время выполнения функции.
'''
Для этого необходимо взять время до начала запуска функции и после ее окончания.
Проверить декоратор для различного рода алгоритмов сортировок на большом наборе данных.
'''

import time
from datetime import datetime

a = 0

def func_duration_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function(my_test_function):
        start = datetime.now()
        function_to_decorate(my_test_function)
        delta = (datetime.now() - start)
        print(delta)
    return the_wrapper_around_the_original_function

def my_test_function(x):
    while x < 100000:
        print ('test')
        x = x + 1

my_test_function_decorated = func_duration_decorator(my_test_function)
my_test_function_decorated(a)