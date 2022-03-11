import sqlFunc

# создание базы данных
connection = sqlFunc.create_connection("D:\\DBPhone.sqlite")

# создание таблиц
sqlFunc.create_table_company(connection)
sqlFunc.create_table_phone(connection)

# заполнение данными
sqlFunc.create_data_company(connection)
sqlFunc.create_data_phone(connection)

# чтение данных
print("")
sqlFunc.selectCompanyCountModel(connection)
# sqlFunc.read_table_users(connection)
# print("")
# sqlFunc.read_table_posts(connection)
# print("")
# sqlFunc.read_users_posts(connection)
# print("")
# sqlFunc.readPostsDescName(connection)
