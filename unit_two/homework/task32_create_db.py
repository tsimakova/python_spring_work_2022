# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg

'''
Ссылка на документацию
https://www.psycopg.org/psycopg3/docs/basic/usage.html
Для подключения использовать пользователя и базу отличную от postgres
'''


# CREATE DATABASE

# import the PostgreSQL client for Python

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to PostgreSQL DBMS

con = psycopg2.connect("user=postgres password='123'");

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

# Obtain a DB Cursor

cursor = con.cursor();

name_Database = "TestSystem2";

# Create table statement

sqlCreateDatabase = "create database " + name_Database + ";"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateDatabase);

# CREATE TABLE

# Connect to the PostgreSQL database server

postgresConnection = psycopg2.connect("dbname=testsystem2 user=postgres password='123'")

# Get cursor object from the database connection

cursor = postgresConnection.cursor()

name_Table = "old_stories"

# Create table statement

sqlCreateTable = "create table " + name_Table + " (id bigint, title varchar(128), summary varchar(256), story text);"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTable)

postgresConnection.commit()
