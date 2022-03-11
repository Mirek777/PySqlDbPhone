import sqlite3
from sqlite3 import Error
import sqlQueryCreate
import sqlQueryAddData
import sqlQuerySelect


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


# ___SQL Извлечение данных___

# общая функция извлечения данных
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


# SQL запрос на возрат все сообщения вместе с комментариями к сообщениям и именами пользователей
def read_phone_models(conn):
    print("# SQL запрос всей таблицы моделей")
    read_table_phone_models = execute_read_query(conn, sqlQuerySelect.read_phone_models)
    for read_table_phone_model in read_table_phone_models:
        print(read_table_phone_model)


# SQL запрос на возрат все сообщения вместе с комментариями к сообщениям и именами пользователей
def selectCompanyCountModel(conn):
    print("# SQL запрос на поиск количества и общей стоимости телефонов каждого производителя")
    number_cost_phones = execute_read_query(conn, sqlQuerySelect.select_number_cost_phones)
    for number_cost_phone in number_cost_phones:
        print(number_cost_phone)


