-- Select certain item that share qualitys
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
