-- Creates a function SafeDiv(a, b) that safely divides two integers.
-- Returns 0 if the divisor (b) is 0 to avoid division by zero errors.
-- Otherwise, returns the integer division result of a DIV b.

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT
BEGIN
    RETURN IF(b = 0, 0, a DIV b);
END$$

DELIMITER ;
