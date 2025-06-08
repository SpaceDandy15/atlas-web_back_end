-- Create a composite index on the first letter of 'name' and the 'score' column
-- This helps optimize queries filtering by name prefix and score simultaneously

CREATE INDEX idx_name_first_score ON names (name(1), score);
