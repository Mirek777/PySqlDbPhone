
# SQL запрос на добавление таблицы компаний
create_table_company = """
CREATE TABLE IF NOT EXISTS company (
  companyId INTEGER PRIMARY KEY AUTOINCREMENT,
  companyName TEXT NOT NULL,
  companyCountry TEXT NOT NULL
);
"""


# SQL запрос на добавление таблицы телефонов
create_table_phone = """
CREATE TABLE IF NOT EXISTS phone (
  phoneId INTEGER PRIMARY KEY AUTOINCREMENT,
  price INTEGER NOT NULL,
  phoneModel TEXT NOT NULL, 
  company_id INTEGER NOT NULL, 
  FOREIGN KEY (company_id) REFERENCES company (companyId)
);
"""