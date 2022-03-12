import sqlFunc

# создание базы данных
connection = sqlFunc.create_connection("D:\\DBPhone.sqlite")

# # создание таблиц
# sqlFunc.create_table_company(connection)
# sqlFunc.create_table_phone(connection)
#
# # заполнение данными
# sqlFunc.create_data_company(connection)
# sqlFunc.create_data_phone(connection)

# чтение данных
print("")
sqlFunc.read_company(connection)
print("")
sqlFunc.read_phone_models(connection)
print("")
sqlFunc.selectCompanyCountModel(connection)
print("")
sqlFunc.highAverCostPhone(connection)
print("")
sqlFunc.countChinesePhone(connection)
