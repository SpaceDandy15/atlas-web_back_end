DELIMITER $$

-- Procedure: ComputeAverageScoreForUser
-- Purpose: Calculate and update the average correction score for a specific user.
-- Input:
--   p_user_id INT - the ID of the user whose average score is computed
-- Steps:
--   1. Compute the average of all scores in the corrections table for the given user.
--   2. Update the users table to set the average_score field to the computed average.
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT  -- Input parameter: ID of the user to compute average score for
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user_id
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the average_score field in the users table for the given user
    UPDATE users 
    SET average_score = avg_score 
    WHERE id = p_user_id;
END$$

DELIMITER ;
