-- Netflix Data Analysis using SQL
-- Solutions of 15 Business Problems

-- 1. Count the number of Movies vs TV Shows
SELECT type, COUNT(*) FROM netflix GROUP BY 1;

-- 2. Most common rating for movies and TV shows
WITH RatingCounts AS (
    SELECT type, rating, COUNT(*) AS rating_count FROM netflix GROUP BY type, rating
),
RankedRatings AS (
    SELECT type, rating, rating_count, RANK() OVER (PARTITION BY type ORDER BY rating_count DESC) AS rank FROM RatingCounts
)
SELECT type, rating AS most_frequent_rating FROM RankedRatings WHERE rank = 1;

-- 3. List all movies released in 2020
SELECT * FROM netflix WHERE release_year = 2020;

-- 4. Top 5 countries with the most content
SELECT * FROM (
    SELECT UNNEST(STRING_TO_ARRAY(country, ',')) AS country, COUNT(*) AS total_content FROM netflix GROUP BY 1
) AS t1 WHERE country IS NOT NULL ORDER BY total_content DESC LIMIT 5;

-- 5. Identify the longest movie
SELECT * FROM netflix WHERE type = 'Movie' ORDER BY SPLIT_PART(duration, ' ', 1)::INT DESC;

-- 6. Content added in last 5 years
SELECT * FROM netflix WHERE TO_DATE(date_added, 'Month DD, YYYY') >= CURRENT_DATE - INTERVAL '5 years';

-- 7. All content by director 'Rajiv Chilaka'
SELECT * FROM (
    SELECT *, UNNEST(STRING_TO_ARRAY(director, ',')) AS director_name FROM netflix
) WHERE director_name = 'Rajiv Chilaka';

-- 8. TV shows with more than 5 seasons
SELECT * FROM netflix WHERE type = 'TV Show' AND SPLIT_PART(duration, ' ', 1)::INT > 5;

-- 9. Count content in each genre
SELECT UNNEST(STRING_TO_ARRAY(listed_in, ',')) AS genre, COUNT(*) AS total_content FROM netflix GROUP BY 1;

-- 10. Average number of content release by India per year (Top 5)
SELECT country, release_year, COUNT(show_id) AS total_release,
ROUND(COUNT(show_id)::numeric / (SELECT COUNT(show_id) FROM netflix WHERE country = 'India')::numeric * 100, 2) AS avg_release
FROM netflix WHERE country = 'India' GROUP BY country, 2 ORDER BY avg_release DESC LIMIT 5;

-- 11. All movies that are documentaries
SELECT * FROM netflix WHERE listed_in LIKE '%Documentaries';

-- 12. Content without a director
SELECT * FROM netflix WHERE director IS NULL;

-- 13. Movies actor 'Salman Khan' appeared in last 10 years
SELECT * FROM netflix WHERE casts LIKE '%Salman Khan%' AND release_year > EXTRACT(YEAR FROM CURRENT_DATE) - 10;

-- 14. Top 10 actors in Indian movies
SELECT UNNEST(STRING_TO_ARRAY(casts, ',')) AS actor, COUNT(*) FROM netflix WHERE country = 'India' GROUP BY 1 ORDER BY 2 DESC LIMIT 10;

-- 15. Categorize content based on 'kill' and 'violence' in description
SELECT category, type, COUNT(*) AS content_count
FROM (
    SELECT *, CASE WHEN description ILIKE '%kill%' OR description ILIKE '%violence%' THEN 'Bad' ELSE 'Good' END AS category FROM netflix
) AS categorized_content
GROUP BY 1, 2 ORDER BY 2;