-- 3-glam_rock.sql
SELECT
    band_name,
    CASE
        WHEN split IS NULL OR split = 0 THEN YEAR(CURDATE()) - formed
        ELSE split - formed
    END AS lifespan
FROM
    metal_bands
WHERE
    main_genre = 'Glam rock'
ORDER BY
    lifespan DESC;
