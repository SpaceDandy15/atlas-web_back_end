-- This index will speed up queries that filter by the first letter of the name, e.g., WHERE name LIKE 'a%'
CREATE INDEX idx_name_first ON names (name(1));