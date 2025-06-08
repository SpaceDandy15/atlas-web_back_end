-- 2-fans.sql
-- Rank country origins of bands ordered by the number of fans (non-unique)

SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
