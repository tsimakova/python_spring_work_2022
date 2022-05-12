
'''
def decorator_render(func):
    def wrapper(name):
        print('Логика перед вызовом')
        func(name)
        print('Логика после вызовом')
    return wrapper

def render(text):
    print(f" функция Render {text.upper()}")

wr = decorator_render(render)
wr('Hi')

'''


def decorator_render(func): # функция декоратор
    print('Call decorator_render')
    def w(text): # вложенная функция
        print('Cal wrapper')
        print('Логика перед вызовом')
        func(text)
        print('Логика после вызова')
    return w

@decorator_render
def render(text):
    print(f" функция Render {text.upper()}")

# wr = decorator_render(render)
# wr('Hi')
render('Hi')