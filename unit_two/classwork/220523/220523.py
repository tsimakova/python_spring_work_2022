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
        return cursor.fetchone()


# Основная программа

access = Database("TestSystem", "postgres", "123", "eric_27", "123")
connection = access.getConnection()
studeniID = access.getStudentID()
print(studeniID)