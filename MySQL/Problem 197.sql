# Write your MySQL query statement below
SELECT Today.id FROM Weather Yesterday
CROSS JOIN Weather Today
WHERE DATEDIFF(Today.recordDate, Yesterday.recordDate) = 1
AND today.temperature > yesterday.temperature