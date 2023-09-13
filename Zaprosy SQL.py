# SELECT c.login, COUNT(*) AS or_num
# FROM "Orders" AS o
# INNER JOIN "Couriers" AS c ON o.courierId = c.id
# WHERE o.inDelivery = true
# GROUP BY c.login;
#
#
# SELECT track,
# 	CASE
# 		WHEN finished = true THEN '2'
# 		WHEN canсelled = true THEN '-1'
# 		WHEN inDelivery = true THEN '1'
# 		ELSE 0
# 	END AS status
# FROM "Orders";