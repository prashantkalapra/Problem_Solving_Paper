"""FIFA WORLD CUP 2026 — Golden Boot Analytics   The FIFA 2026 analytics database has a 
table: GOALS(goal_id, player_name, country, match_id, minute_scored, goal_type ['Open 
Play'/'Penalty'/'Free Kick'/'Own Goal']). Tournament organizers need to find the Golden Boot winner (most 
goals, excluding own goals) and identify which country scores the most goals in the second half (minute > 
45). 
                                                                                            
Write SQL queries for: (a) Find the Golden Boot winner — the player with the most goals excluding 'Own 
Goal' type. Handle ties by also showing the player with fewer penalty goals as the tiebreaker. (b) Find the 
country that scored the most goals in the second half (minute_scored > 45), excluding own goals. (c) Using a 
window function, rank all players by goal count within their country — so we can see the top scorer per 
country. 

"""



(a) Find the Golden Boot winner — the player with the most goals excluding 'Own 
Goal' type. Handle ties by also showing the player with fewer penalty goals as the tiebreaker. 


SELECT
    player_name,
    country,
    COUNT(*) AS total_goals,
    SUM(CASE WHEN goal_type = 'Penalty' THEN 1 ELSE 0 END) AS penalty_goals
FROM GOALS
WHERE goal_type <> 'Own Goal'
GROUP BY player_name, country
ORDER BY total_goals DESC, penalty_goals ASC
LIMIT 1;

(b) Find the country that scored the most goals in the second half (minute_scored > 45), excluding own goals.

select country,sum(goal_type) from goals
where goal_type <> 'own goals' and 
minnute_scored > 45 group by country 
order by desc ;

(c) Using a window function, rank all players by goal count within their country — so we can see the top scorer per 
country. 

SELECT
    country,
    player_name,
    total_goals,
    RANK() OVER (
        PARTITION BY country
        ORDER BY total_goals DESC
    ) AS player_rank
FROM (
    SELECT
        country,
        player_name,
        COUNT(*) AS total_goals
    FROM GOALS
    WHERE goal_type <> 'Own Goal'
    GROUP BY country, player_name
) AS player_stats
ORDER BY country, player_rank;

