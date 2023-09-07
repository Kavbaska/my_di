# SELECT c.id, COUNT(o.inDelivery)
# FROM "Orders" AS o
# INNER JOIN "Couriers" AS c ON o.courierId = c.id
# WHERE o.inDelivery = true
# GROUP BY c.id;
#
#
# SELECT track,
# 	CASE
# 		WHEN finished == true
# 		WHEN canсelled == true
# 		WHEN inDelivery == true
# 		ELSE 0
# 	END AS status
# FROM "Orders";