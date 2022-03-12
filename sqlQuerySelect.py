# SQL запрос таблицы производителей
read_company_table = """
SELECT
  companyName,
  companyCountry
FROM
  company
ORDER BY
  companyName
"""

# SQL запрос всей таблицы моделей
read_phone_models = """
SELECT
  companyName, phoneModel, price, companyCountry, companyId
FROM
  company
LEFT JOIN
  phone
ON 
  company.companyId = phone.company_id
ORDER BY 
  1 
"""

# SQL запрос на поиск количества и общей стоимости телефонов каждого производителя
select_number_cost_phones = """
SELECT
  companyName AS company,
  COUNT (company_id) AS phone,
  SUM (COALESCE(phone.price, 0)) AS phone
FROM
  company
LEFT JOIN
  phone
ON 
  company.companyId = phone.company_id
GROUP BY
  companyName
"""

# SQL запрос на поиск производителя с наибольшей средней стоимостью телефона этого производителя
high_average_cost_phone = """
SELECT 
  companyName, 
  AVG(price) 
FROM 
  phone,
  company
WHERE
  company.companyId = phone.company_id
GROUP BY
  companyId
ORDER BY 2 DESC LIMIT 1
"""

# SQL запрос на определения количества китайских товаров
count_chinese_phone = """
SELECT
  companyCountry,
  COUNT (company_id)
FROM
  company
LEFT JOIN
  phone
ON
  company.companyId = phone.company_id
GROUP BY
  companyCountry
"""