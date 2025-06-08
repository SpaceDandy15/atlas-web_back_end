-- 0-uniq_users.sql
-- Create users table with id as primary key, email unique and not null, name with max 255 chars
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
