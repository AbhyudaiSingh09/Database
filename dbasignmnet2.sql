SELECT name,club,country from players where country= "'USA'" and Position = "'Midfielder'";

Select Name,Club,Country,TIMESTAMPDIFF(YEAR,DOB,CURDATE()) as age from players as p ,match_results as m where IS_Captain = '1' and date_Of_match like '2014%';


Select Country_Name from country as c, match_results as m where No_of_Worldcup_won >2 and date_of_match like '2014%';

select Country_Name from country as c, match_results as m where No_of_Worldcup_won =0 and date_of_match like '2014%';

select Name,Country from players as p,match_results as m WHERE date_of_match  like '2014%' and  NOT  EXISTS  (SELECT * FROM player_cards WHERE  player_cards.player_ID=p.player_id);

select distinct Name,Country from players as p,match_results as m,player_cards as c WHERE p.player_id = c.player_id and date_of_match  like '2014%' and  red_cards = '1';
select Name,Country from players as p,match_results as m WHERE date_of_match  like '2014%' and  EXISTS  (SELECT MAX(red_cards) FROM player_cards WHERE  player_cards.player_ID=p.player_id ); 


SELECT host_city, Count(*) as Games_played from match_results group by host_city;

SELECT host_city, Count(*) as Games_played from match_results group by host_city order by Games_played desc;

SELECT Country_Name, Count(*) as number_of_games, Sum(Team1_Score), Sum(Team2_Score)
FROM country
INNER JOIN match_results
ON Team1 = Country_Name
GROUP BY Country_Name;


SELECT Country_Name, Count(*) as number_of_games, Sum(Team1_Score), Sum(Team2_Score) FROM country INNER JOIN match_results ON Team2 = Country_Name GROUP BY Country_Name;

create view  TEAM_SUMMARY as select country_name as CountryName,count(country_name) as NoOfGames,sum(team1_score) as TotalGoalsFor,sum(team2_score) as TotalGoalsAgainst from country inner join match_results on country.country_name = match_results.team1 or country.country_name = match_results.team2 group by country_name order by count(country_name) desc;

SELECT m.date_of_match,m.team1,m.team2,abs(team1_score-team2_score)as score_difference, IF (team1_score>team2_score,team1,team2) as Winning_team from match_results as m;

select * from match_results where team1="'Brazil'" or team2="'Brazil'";

SELECT players.name, players.country, player_assists_goals.Goals
from players
INNER JOIN player_assists_goals
ON players.Player_id = player_assists_goals.Player_id
WHERE player_assists_goals.Goals >= 1
ORDER BY player_assists_goals.Goals DESC;

SELECT players.name, players.country, player_assists_goals.Goals
from players
INNER JOIN player_assists_goals
ON players.Player_id = player_assists_goals.Player_id
WHERE player_assists_goals.Goals > 2
ORDER BY player_assists_goals.Goals DESC;

select Country_Name, Population from country group by country_name order by population desc;

INSERT INTO country (Country_Name,Population,No_Of_Worldcup_won,Manager) values('test_country',123.3,2,'test_manager');
INSERT INTO country (Country_Name,Population,No_Of_Worldcup_won,Manager) values('test',124.3,2,'manager');
INSERT INTO country (Country_Name,Population,No_Of_Worldcup_won,Manager) values('country',125.3,2,'testmanager');
