-- Create a function SafeDiv that divides 'a' by 'b'
-- Returns 0 if 'b' is 0 to avoid division by zero errors

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    -- If b is zero, return 0; otherwise, return the division result
    RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;
