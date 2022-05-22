
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

action = input("Выберите действие:\n"
               "1. Войти.\n"
               "2. Зарегистрироваться.\n")

if int(action) == 1:
    lgn = str(input("Введите имя пользователя: "))
    psw = str(input("Введите пароль : "))
    con = psycopg2.connect("user=postgres password='123'");
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = con.cursor();
    name_Database = "TestSystem";
    postgresConnection = psycopg2.connect("dbname=TestSystem user=postgres password='123'")
    cursor = postgresConnection.cursor()
    name_Table = "credential"
    cursor.execute("select * from student where id_student = (select id_student from credential where login like %s and password like %s)", [lgn, psw])
    name = cursor.fetchone()
    if name is None:
        print('Проверьте корректность введенных учетных данных.')
    else:
        print('Добро пожаловать, ' + name[1] + ' ' + name[2] + '!\nВыберите тему теста:')
        cursor.execute("select * from test")
        tests = cursor.fetchall()
        for i in tests:
            print('№' + str(i[0]) + '. ' + str(i[1]) + '.')

elif int(action) == 2:
    con = psycopg2.connect("user=postgres password='123'");
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = con.cursor();
    name_Database = "TestSystem";
    postgresConnection = psycopg2.connect("dbname=TestSystem user=postgres password='123'")
    cursor = postgresConnection.cursor()
    name_Table = "student"
    lgn = str(input('Введите имя пользователя:'))
    psw = str(input('Введите пароль:'))
    name = str(input('Введите свое имя:'))
    surname = str(input('Введите свою фамилию:'))
    patronym = str(input('Введите свое отчество:'))
    age = int(input('Введите свой возраст:'))
    sex = 'True'
    group = str(input('Введите номер группы:'))
    cursor.execute("select id_student from student")
    ids = cursor.fetchall()
    id_new = (len(ids)) + 1
    cursor.execute("insert into student values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [str(id_new), name, surname, patronym, age, sex, group, '1', '1', '1'])
    cursor.execute("select * from student where id_student = 4")
    stud = cursor.fetchall()
    #print(stud)
    cursor.execute("insert into credential values (%s, %s, %s, %s)", [str(id_new), lgn, psw, str(id_new)])
    cursor.execute("select * from credential where id_student = 4")
    creds = cursor.fetchone()
    #print(creds)
    print('Поздравляю, вы успешно зарегистрированы!\nВаши учетные данные:')
    print('Имя пользователя: ' + str(creds[1]) + '\n' + 'Пароль: ' + str(creds[2]))

else:
    print('Некорректный ввод. Начните сначала.')

