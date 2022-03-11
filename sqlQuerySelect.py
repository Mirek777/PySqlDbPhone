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
  *
FROM
  phone
ORDER BY
  company_id
"""


# SQL запрос на поиск количества и общей стоимости телефонов каждого производителя
select_number_cost_phones = """
SELECT
  companyName,
  COUNT (company_id),
  SUM (COALESCE(phone.price, 0))
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
  price 
FROM
  company,
  phone
WHERE
  company.companyId = phone.company_id
ORDER BY
  companyName
"""
