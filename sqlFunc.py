import sqlite3
from sqlite3 import Error
import sqlQueryCreate
import sqlQueryAddData
# import sqlQueryRead
# import sqlQueryJoin

# ___Обшие___

# ___SQL___


# запуск сервера
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e} occurred")
    return connection


# общая функция для формирование таблиц
def excecute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query excecuted successfuly")
    except Error as e:
        print(f"The error '{e} occured")


# ___SQL Создание таблиц___

# функция для создания таблицы юзеров
def create_table_company(conn):
    excecute_query(conn, sqlQueryCreate.create_table_company)


# функция для создания таблицы постов
def create_table_phone(conn):
    excecute_query(conn, sqlQueryCreate.create_table_phone)


# ___SQL Добавление данных___

# функция для добавления данных в таблицу компаний
def create_data_company(conn):
    excecute_query(conn, sqlQueryAddData.add_company)


# функция для добавления данных в таблицу телефонов
def create_data_phone(conn):
    excecute_query(conn, sqlQueryAddData.add_phone)

#
# # ___SQL Извлечение данных___
#
# # общая функция извлечения данных
# def execute_read_query(connection, query):
#     cursor = connection.cursor()
#     result = None
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"The error '{e}' occurred")
#
#
# # функция извлечения данных из таблицы всех юзеров
# def read_table_users(conn):
#     users = execute_read_query(conn, sqlQueryRead.select_users)
#     for user in users:
#         print(user)
#
#
# # функция извлечения данных из таблицы всех постов
# def read_table_posts(conn):
#     posts = execute_read_query(conn, sqlQueryRead.select_posts)
#     for post in posts:
#         print(post)
#
#
# # SQL запрос на возрат идентификаторов, имен пользователей и описание сообщений этих пользователей
# def read_users_posts(conn):
#     users_posts = execute_read_query(conn, sqlQueryJoin.select_users_posts)
#     for users_post in users_posts:
#         print(users_post)
#
#
# # SQL запрос на возрат все сообщения вместе с комментариями к сообщениям и именами пользователей
# def readPostsDescName(conn):
#     posts_comments_users = execute_read_query(conn, sqlQueryJoin.select_posts_comments_users)
#
#
