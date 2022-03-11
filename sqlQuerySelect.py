# SQL запрос на поиск количества и общей стоимости телефонов каждого производителя
select_number_cost_phones = """
SELECT
  companyName as company,
  COUNT(company_id) as phone
FROM
  company,
  phone
WHERE
  company.companyId = phone.company_id
GROUP BY
  phone.company_id
"""
#
# select_post_likes = """
# SELECT
#   description as Post,
#   COUNT(likes.id) as Likes
# FROM
#   likes,
#   posts
# WHERE
#   posts.id = likes.post_id
# GROUP BY
#   likes.post_id
# """
