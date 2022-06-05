'''
# todo: 1 Реализовать итератор на базе класса Person.

class Profile:
    def __init__(self,  id, login,  password,  name,  age):
        self.id = id
        self.login = login
        self.__password = password
        self.name = name
        self.age = age

# Объект класса должен итерироваться циклом for
obj = Profile( 1, "admin", 123456, "Peter", 25 )
for i in obj:
    # функция должна выводить название и значение атрибута
    print(i)

2 Реализовать генератор на базе класса Profile. При итерировании циклом метод
должен выводить название и значение атрибута

3 Реализовать контекстный менеджер над DB . Класс должен возвращать соединение с БД
'''

# Итератор

# Генератор

class Profile:
    def __init__(self,  id, login,  password,  name,  age):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.age = age


    def __iter__(self):
        yield "id: " + str(self.id)
        yield "login: " + str(self.login)
        yield "password: " + str(self.password)
        yield "name:" + str(self.name)
        yield "age:" + str(self.age)

obj = Profile( 1, "admin", 123456, "Peter", 25 )

for i in obj:
    print(i)

# Контекстный менеджер

import psycopg2

class DB:
    """Класс содержит атрибуты и методы для подключения к SQL СУБД."""
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)
            return self.conn
        except psycopg2.OperationalError:
            pass

    def __exit__(self, db_name, db_user, db_password):
        self.conn.commit()
        self.conn.close()


mydb = DB("TestSystem", "postgres", "123")
with mydb as conn:
    cursor = conn.cursor()
    cursor.execute("select * from profile")
    answer = cursor.fetchall()
    print(answer)
