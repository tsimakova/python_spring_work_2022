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
    def __init__(self, db_name, db_user, db_password, user_login, user_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.user_login = user_login
        self.user_password = user_password

    # Метод создания соединения с базой по учетным данным.
    def getConnection(self):
        return psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)

    # Метод получения номера студента по логину и паролю.
    def getStudentID(self):
        connection = self.getConnection() # Метод класса использует (ссылается на) ранее определенный метод того же класса.
        cursor = connection.cursor()
        cursor.execute("select id_student from credential where login like %s and password like %s", [self.user_login, self.user_password])
        student_id = cursor.fetchone()
        return int(student_id[0])

    def getStudentProfile(self):
        st_id = self.getStudentID()
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select * from student where id_student = %s", [st_id])
        return cursor.fetchone()

# Основная программа

access = Database("TestSystem", "postgres", "123", "eric_27", "123")
connection = access.getConnection()
studentID = access.getStudentID()
studentProfile = access.getStudentProfile()
print(studentID)
print(studentProfile)