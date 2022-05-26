import psycopg2

class Database:
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    def getConnection(self):
        connection = psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)
        cursor = connection.cursor()
        return cursor

class Authentification:
    def __init__(self, user_login, user_password, cursor):
        self.user_login = user_login
        self.user_password = user_password
        self.cursor = cursor
    def login(self):
        auth_status = False
        self.user_login = str(input("Введите имя пользователя: "))
        self.user_password = str(input("Введите пароль : "))
        self.cursor.execute("select id_student from credential where login like %s and password like %s", [self.user_login, self.user_password])
        id_student = cursor.fetchone()
        if id_student is not None:
            self.auth_status = True
            return (id_student[0], auth_status)
        else:
            self.auth_status = False
            return ("Unrecognized", auth_status)
    def createUser(self):
        auth_status = False
        lgn = str(input('Введите имя пользователя:'))
        psw = str(input('Введите пароль:'))
        cursor.execute("select id_student from student")
        ids = cursor.fetchall()
        id_new = (len(ids)) + 1
        self.cursor.execute("insert into credential values (%s, %s, %s, %s)", [str(id_new), lgn, psw, str(id_new)])
        name = str(input('Введите свое имя:'))
        surname = str(input('Введите свою фамилию:'))
        patronym = str(input('Введите свое отчество:'))
        age = int(input('Введите свой возраст:'))
        sex = 'True'
        group = str(input('Введите номер группы:'))

        pass
    def logout(self):
        pass


# Start

#action = input("Выберите действие:\n"
 #              "1. Войти.\n"
  #             "2. Зарегистрироваться.\n")


action = 1
#action = 2

if action == 1:
    access = Database("TestSystem", "postgres", "123")
    cursor = access.getConnection()
    creds = Authentification('eric_27', '123', cursor)
    idn = creds.login()
    print(idn)
elif action == 2:
    pass
else:
    pass






'''
class TestSystem:
    def __init__(self):
        pass

class Test:
    def __init__(self, id_test, theme):
        pass
    def getListTest:
        pass
    def getTest:
'''




