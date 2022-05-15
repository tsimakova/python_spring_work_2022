#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения

'''
Пример:
render, 10,  12.05.2022 12:00
show,    5,  12.05.2022 12:02
render, 15,  12.05.2022 12:07

Декоратор должен применяться для различных функций с переменным числом аргументов.
Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

'''
from datetime import datetime

def counter(function_to_decorate):
    global wrapper_count
    wrapper_count = 0
    def wrapper(*args, **kwargs):
        global wrapper_count
        global function
        global date
        global time
        wrapper_count = wrapper_count + 1
        function = function_to_decorate.__name__
        date = (datetime.now()).strftime('%d.%m.%Y')
        time = (datetime.now()).strftime('%H:%M')
        return function_to_decorate
    return wrapper

def my_sum_function(x, y):
    z = x + y
    return z

my_decorated_function = counter(my_sum_function)

a = 3
b = 2
print(my_decorated_function(a, b))
c = 9
d = 4
print(my_decorated_function(c, d))

print(function)
print(str(wrapper_count))
print(str(date))
print(str(time))

log = open('D:\PYTHON_course\debug.log', 'a')
log.write(str(function) + ', ' + str(wrapper_count) + ', ' + str(date) + ' ' + str(time) + '\n')
log.close()

