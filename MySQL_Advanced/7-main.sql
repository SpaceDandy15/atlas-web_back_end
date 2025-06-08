-- Show initial data
SELECT * FROM users;
SELECT * FROM corrections;

SELECT "--";

-- Call procedure for Jeanne
CALL ComputeAverageScoreForUser((SELECT id FROM users WHERE name = "Jeanne"));

SELECT "--";

-- Show users after average score update
SELECT * FROM users;
