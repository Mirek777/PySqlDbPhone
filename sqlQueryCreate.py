
# SQL запрос на добавление таблицы компаний
create_table_company = """
CREATE TABLE IF NOT EXISTS company (
  companyId INTEGER PRIMARY KEY AUTOINCREMENT,
  companyName TEXT NOT NULL,
  companyCountry TEXT
);
"""

# SQL запрос на добавление таблицы телефонов
create_table_phone = """
CREATE TABLE IF NOT EXISTS phone(
  phoneId INTEGER PRIMARY KEY AUTOINCREMENT, 
  phoneModel TEXT NOT NULL, 
  FOREIGN KEY (companuId) REFERENCES company (id),
  price INTEGER NOT NULL
);
"""