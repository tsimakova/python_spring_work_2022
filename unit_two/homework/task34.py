'''
#todo: Реализовать классы DB и Profile
class DB:
    Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     (атрибуты доступа к БД) . Метод возвращает соединение.
    __init__(self, dbname, user, password):
        # В констукторе инициализируем атрибуты доступа к БД
        pass
    def get_connect(self):
        # Метод возвращает соединение к БД
        pass
class Profile:
    Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно
    # В констукторе инициализируем атрибуты сущности Profile
    __init__(self, login, password, name, surname, age, tel, email):
        pass
    # в аргументе conn передается дискриптор подключения к БД
    def set_profile(self, conn):
        # Добавляет профиль в БД
        pass
    def get_profile(self, conn):
        # Извлекает профиль из БД
        pass
'''


import psycopg2

# Создание класса

class Database:
    # Инициализация атрибутов (данных), которые будут обрабатываться определенными в классе методами (функциями).
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password

    # Метод создания соединения с базой по учетным данным.
    def getConnection(self):
        return psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)

    # Метод получения профиля пользователя по логину и паролю.
    def getProfile(self, user_login, user_password):
        self.user_login = user_login
        self.user_password = user_password
        connection = self.getConnection() # Метод класса использует (ссылается на) ранее определенный метод того же класса.
        cursor = connection.cursor()
        cursor.execute("select * from profile where login like %s and password like %s", [self.user_login, self.user_password])
        user = cursor.fetchall()
        return user

    # Метод создания в базе нового пользователя.
    def setProfile(self, id_group, name, surname, patronym, age, login, password):
        self.id_group = id_group
        self.name = name
        self.surname = surname
        self.patronym = patronym
        self.age = age
        self.login = login
        self.password = password
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select id_profile from profile")
        users = cursor.fetchall()
        id_new = len(users) + 1
        cursor.execute("insert into profile (id_profile, id_group, name, surname, patronym, age, login, password) values (%s, %s, %s, %s, %s, %s, %s, %s)", [str(id_new), self.id_group, self.name, self.surname, self.patronym, self.age, self.login, self.password])
        print('Поздравляю, вы успешно зарегистрированы!\nВаши учетные данные:')
        connection.commit()
        cursor.execute("select * from profile where id_profile = %s", [id_new])
        new_user = cursor.fetchall()
        return new_user
        cursor.close()
        connection.close()




# Основная программа

access = Database("TestSystem", "postgres", "123")
connection = access.getConnection()
user = access.getProfile("ivan_25", "000")
print(user)
new_user = access.setProfile("245", "Тамара", "Симакова", "Сергеевна", "30", "tamara_37", "567")
print(new_user)