
-- Top skills
SELECT skill, COUNT(*) demand
FROM job_market.jobs_processed
CROSS JOIN UNNEST(SPLIT(skills, ',')) AS t(skill)
GROUP BY skill
ORDER BY demand DESC;

-- City distribution
SELECT location, COUNT(*)
FROM job_market.jobs_processed
GROUP BY location
ORDER BY COUNT(*) DESC;
