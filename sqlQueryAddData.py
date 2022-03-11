
# SQL запрос на добавление данных в таблицу компаний
add_company = """
INSERT INTO
  company (companyId, companyName, companyCountry)
VALUES
  (20, 'Apple', 'USA'),
  (33, 'Xiaomi', 'China'),
  (11, 'Nokia', 'Finland'),
  (444, 'Samsung', 'South Korea'),
  (8, 'Huawei', 'China');
"""

# SQL запрос на добавление данных в таблицу телефонов
add_phone = """
INSERT INTO
  phone (phoneId, phoneModel, company_id, price)
VALUES
  (43, 'iPhone 13 Pro Max', 20, 135000),
  (18, 'iPhone SE', 20, 105000),
  (16, 'iPhone XS', 20, 35000),
  (40, '1100', 11, 5000),
  (4, 'Asha 311', 11, 3000),
  (88, 'Mi 5X', 33, 11000),
  (83, 'Mi 8', 33, 10000),
  (64, 'P50 Pro', 8, 21000),
  (11, 'Nova 9', 8, 22000);
"""