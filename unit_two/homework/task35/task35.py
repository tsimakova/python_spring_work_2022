import psycopg2

class DB:
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    def getConnection(self):
        return psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)

class Auth(DB):
    auth_status = False
    def __init__(self):
        pass

    def registration(self):
        id_group = str(input("Введите номер группы: "))
        name = str(input("Введите имя: "))
        surname = str(input("Введите фамилию: "))
        patronym = str(input("Введите отчество: "))
        age = str(input("Введите возраст: "))
        login = str(input("Введите логин: "))
        password = str(input("Введите пароль: "))
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select id_profile from profile")
        users = cursor.fetchall()
        id_new = len(users) + 1
        cursor.execute("insert into profile (id_profile, id_group, name, surname, patronym, age, login, password) values (%s, %s, %s, %s, %s, %s, %s, %s)", [str(id_new), id_group, name, surname, patronym, age, login, password])
        print('Поздравляю, вы успешно зарегистрированы!\nВаши учетные данные:')
        connection.commit()
        cursor.execute("select * from profile where id_profile = %s", [id_new])
        new_user = cursor.fetchall()
        return new_user[0]
        cursor.close()
        connection.close()

    def login(self):
        user_login = str(input("Введите имя пользователя: "))
        user_password = str(input("Введите пароль : "))
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select * from profile where login like %s and password like %s", [user_login, user_password])
        user = cursor.fetchall()
        if cursor.rowcount == 1:
            auth_status = True
            welcome = "Добро пожаловать, " + str(user[0][2] + " " + str(user[0][4]) + "!")
            return welcome
        else:
            Auth.auth_status = False
            deny = "Пользователь не найден. Проверьте правильность введенных учетных данных."
            return deny

    def logout(self):
        Auth.auth_status = False



access = DB("TestSystem", "postgres", "123")
connection = access.getConnection()
#user = Auth.login(access)
new_user = Auth.registration(access)
print(new_user)






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



# 27.05.22

# class View:
#     def render(self):
#         pass
#
# class TestsView(View):
#     def __init__(self, template, data):
#         self.template =
#         self.data  = data
#         pass
#     def render(self):
#         # Логика вывода тестов в консоль
#         cursor.execute("select * from test")
#         data = cursor.fetchall()
#         tests_view = template(data)
#         print(tests_view)
#
# class QuestionView(View):
#     def __init__(self, id_test, theme):
#         self.id_test = id_test
#         self.theme = theme
#     def render(self):
#         # Логика вывода вопросов в консоль
#         cursor.execute("select * from question")
#         data = cursor.fetchall()
#         question_view = template(data)
#         print(tests_view)

