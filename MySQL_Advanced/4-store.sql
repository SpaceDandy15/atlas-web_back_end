-- Trigger to update item quantity after an order is inserted
DELIMITER $$
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$
DELIMITER ;
