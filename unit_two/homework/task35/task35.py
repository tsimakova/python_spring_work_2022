import sys

import psycopg2

class DB:
    """Класс содержит атрибуты и методы для подключения к SQL СУБД."""
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    def getConnection(self):
        return psycopg2.connect(dbname = self.db_name, user = self.db_user, password =self.db_password)

class Auth(DB):
    """Класс содержит атрибуты и методы для аутентификации пользователя в системе TestSystem и выхода из нее."""
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
        for i in new_user:
            return str("ID пользователя - " + str(i[0]) + "\n" + "Номер группы - " + str(i[1]) + "\n" + "Имя - " + i[2] + "\n" + "Фамилия - " + i[3] + "\n" + "Отчество - " + i[4] + "\n" + "Возраст - " + str(i[5]) + "\n" + "Логин - " + i[6] + "\n" + "Пароль - " + str(i[7]))
        cursor.close()
        connection.close()

    def login(self):
        user_login = str(input("Введите имя пользователя: "))
        user_password = str(input("Введите пароль: "))
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select * from profile where login like %s and password like %s", [user_login, user_password])
        user = cursor.fetchall()
        if cursor.rowcount == 1:
            Auth.auth_status = True
            welcome = "Добро пожаловать, " + str(user[0][2] + " " + str(user[0][4]) + "!")
            return welcome
        else:
            Auth.auth_status = False
            print("Пользователь не найден. Проверьте правильность введенных учетных данных.")
            sys.exit()
        cursor.close()
        connection.close()

    def logout(self):
        Auth.auth_status = False


class Test(DB):
    """Класс содержит атрибуты и методы для выполнения запросов в БД TestSystem. В классе реализован следующий функционал:
    - Получение списка всех доступных тестов;
    - Получение списка вопросов для заданного теста;
    - Получение заданного вопроса и списка ответов к нему;
    - Выбор ответа."""
    def __init__(self):
        pass

    def getTests(self):
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select * from test")
        tests_list = cursor.fetchall()
        return tests_list
        cursor.close()
        connection.close()

    def getQuestions(self):
        global selected_test
        selected_test = int(input("Выберите номер теста: "))
        connection = self.getConnection()
        cursor = connection.cursor()
        cursor.execute("select id_question, question_text from question where id_test = %s", [selected_test])
        questions_list = cursor.fetchall()
        if len(questions_list) != 0:
            return questions_list
        else:
            print("Ошибка, выбран не существующий тест!")
            sys.exit()
        cursor.close()
        connection.close()

    def getQuestion(self):
        global remained_questions
        global selected_question
        connection = DB.getConnection(self)
        selected_question = str(input("Выберите номер вопроса: "))
        cursor = connection.cursor()
        cursor.execute("select question_text from question where id_test = %s and id_question = %s", [selected_test, selected_question])
        question_view = cursor.fetchone()
        if question_view is not None:
            cursor.execute("select id_answer, answer_text from answer where id_question = %s", [selected_question])
            answers_view = cursor.fetchall()
            print("Вопрос " + selected_question + ": " + question_view[0])
            print("Варианты ответа:")
            answers_string = '\n'.join((str(i[0]) + ". " + str(i[1]) + ".") for i in answers_view)
            cursor.execute("select id_question, question_text from question where id_test = %s and id_question != %s", [selected_test, selected_question])
            remained_questions = cursor.fetchall()
            return (answers_string, remained_questions)
        else:
            print("Ошибка, выбран не существующий вопрос!")
            sys.exit()
        cursor.close()
        connection.close()

    def setAnswer(self):
        connection = DB.getConnection(self)
        selected_answer = str(input("Выберите номер ответа: "))
        cursor = connection.cursor()
        cursor.execute("select correctness from answer where id_question = %s and id_answer = %s", [selected_question, selected_answer])
        answer_view = cursor.fetchone()
        if answer_view is not None:
            return answer_view[0]
        else:
            print("Ошибка, выбран не существующий ответ!")
            sys.exit()
        cursor.close()
        connection.close()

class View:
    """Класс содержит атрибуты и методы для формирования представления списка тестов и списква вопросов. """
    def render(self):
        pass

class TestsView(View):
    def render(self, tests_list):
        self.tests_list = tests_list
        tests_view = '\n'.join((str(i[0]) + '. ' + str(i[1]) + ".") for i in tests_list)
        print("Доступны следующие тесты:")
        return tests_view

class QuestionsView(View):
    def render(self, questions_list):
        self.questions_list = questions_list
        questions_view = '\n'.join((str(i[0]) + '. ' + str(i[1]) + ".") for i in questions_list)
        return questions_view

class TestSystem(Test):
    """Класс содержит атрибуты и методы для реализиции бизнес-логики TestSystem: выбор и прохождение тестов, учет ответов, оценка результатов теста. """
    def __init__(self):
        pass
    
    def runTest(self):
        result = []
        tests = Test.getTests(self)
        test_view = TestsView.render(self, tests)
        print(test_view)
        questions = Test.getQuestions(self)
        #print(questions)
        qnumber = 0
        try_number = len(questions)
        while qnumber < try_number:
            questions_view = QuestionsView.render(self, questions)
            print(questions_view)
            question_view = Test.getQuestion(self)
            print(question_view[0])
            answer_view = Test.setAnswer(self)
            if answer_view == True:
                print("Ответ верный!")
            else:
                print("Ответ неверный!")
            result.append(answer_view)
            qnumber = qnumber + 1
            questions = remained_questions
        else:
            print("Тест завершен!")
            return ("Число правильных ответов: " + str(result.count(True)) + " из " + str(try_number))

# Код программы.

access = DB("TestSystem", "postgres", "123")
connection = access.getConnection()
start = input("Выберите опцию:" + "\n" + "1. Авторизация." + "\n" + "2. Регистрация." + "\n" + "Ваш ответ: ")
if start.isalpha() == True:
    print("Некорректный ввод, введите номер опции.")
else:
    if int(start) == 1:
        auth = Auth.login(access)
        print(auth)
        test = TestSystem.runTest(access)
        print(test)
    elif int(start) == 2:
        new_user = Auth.registration(access)
        print(new_user)
        test = TestSystem.runTest(access)
        print(test)
    else:
        print("Некорректный ввод, введите номер опции.")






