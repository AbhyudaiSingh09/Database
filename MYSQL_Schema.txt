
CREATE TABLE COUNTRY(
    Country_Name Varchar(50),
    Population decimal(25,2),
    No_of_Worldcup_won int,
    Manager varchar(50),
    PRIMARY KEY(Country_Name)
    );
    
    
CREATE TABLE Players(
	Player_ID int,
    Name varchar(40),
    Fname varchar(20),
    Lname varchar(35),
    DOB date,
    Country varchar(20),
    Heightcms int,
    Club varchar(30),
    Position varchar(10),
    Caps_for_Country int,
    IS_CAPTAIN Boolean,
    PRIMARY KEY(Player_ID),
    FOREIGN KEY (Country) REFERENCES COUNTRY(Country_Name)
    );
    
    
    
    
CREATE TABLE MATCH_RESULTS(
	Match_ID int,
    Date_of_Match date,
    Start_Time_Of_Match time,
    Team1 varchar(25),
    Team2 varchar(25),
    Team1_score int,
    Team2_score int,
    Stadium_name varchar(35),
    Host_City varchar(20),
    Primary key (Match_ID),
    Foreign Key (Team1) REFERENCES COUNTRY(Country_Name),
    Foreign Key (Team2) REFERENCES COUNTRY(Country_Name)
);

CREATE TABLE PLAYER_CARDS(
	Player_ID int,
    Yellow_Cards int,
    Red_Cards int,
    PRIMARY KEY (Player_ID),
    Foreign Key (Player_ID) REFERENCES Players(Player_ID)
);

CREATE TABLE Player_Assist_Goals(
	Player_ID int,
    No_of_Matches int,
    Goals int,
    Assists int,
    Minutes_played int,
    PRIMARY KEY (Player_ID),
    Foreign Key (Player_ID) REFERENCES Players(Player_ID)
)
