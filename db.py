import csv
from re import M
from sqlite3 import Date
import string
from tkinter import Label
import mysql.connector


mysql= mysql.connector.connect(
    host = 'academicmysql.mysql.database.azure.com',
    user= 'axs7941',
    password = 'ABHYUDAIsingh9', 
    )

cursor = mysql.cursor()

cursor.execute("use axs7941;")


# #########################################################################
# # ADD DATA TO COUNTRY TABLE 
# #########################################################################

# with open('country.csv','r') as csv_file:
#     csv_reader= csv.reader(csv_file)

#     for line in csv_reader:
#         Country_Name=line[0]
#         print(Country_Name)
#         Population = line[1]
#         print(Population)
#         No_of_Worldcup_won =line[2]
#         print(No_of_Worldcup_won)
#         Manager =line[3]
#         print(Manager)
#         cursor.execute("INSERT INTO COUNTRY(Country_Name, Population, No_of_Worldcup_won, Manager) VALUES (%s,%s,%s,%s)",(Country_Name,Population,No_of_Worldcup_won,Manager))
#         mysql.commit()
#     print("Done")



# ########################################################################
# #ADD DATA TO PLAYERS TABLE 
# ########################################################################

# with open('Players.csv','r') as csv_file:
#     csv_reader= csv.reader(csv_file)

#     for line in csv_reader:
#         Player_ID = line[0]
#         Name = line[1]
#         Fname = line[2]
#         Lname = line[3]
#         DOB = line[4]
#         Country = line[5]
#         Height = line[6]
#         Club = line[7]
#         Position = line[8]
#         Caps_for_Country = line[9]
#         IS_Captain = line[10]
#         cursor.execute("INSERT INTO Players(Player_ID,Name,Fname,Lname,DOB,Country,Heightcms,Club,Position,Caps_for_Country,IS_Captain) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Player_ID,Name,Fname,Lname,DOB,Country,Height,Club,Position,Caps_for_Country,IS_Captain))
#         mysql.commit()
#     print("Done")





# cursor.execute("SELECT * FROM PLAYERS;")
# data = cursor.fetchall()
# print(data)

#################################################################################################################################################################

#########################################################################
#ADD DATA TO MATCH_RESULTS TABLE 
#########################################################################

# with open('Match_results.csv','r') as csv_file:
#     csv_reader= csv.reader(csv_file)

#     for line in csv_reader:
#         Match_ID = line[0]
#         Date_of_Match = line[1]
#         Start_Time_Of_Match = line[2]
#         Team1 = line[3]
#         Team2 = line[4]
#         Team1_score = line[5]
#         Team2_score = line[6]
#         Stadium_name = line[7]
#         Host_City = line[8]
#         cursor.execute("INSERT INTO MATCH_RESULTS(Match_ID,Date_of_Match,Start_Time_Of_Match,Team1,Team2,Team1_score,Team2_score,Stadium_name,Host_City) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Match_ID,Date_of_Match,Start_Time_Of_Match,Team1,Team2,Team1_score,Team2_score,Stadium_name,Host_City))
#         mysql.commit()
#     print("Done")





# cursor.execute("SELECT * FROM MATCH_RESULTS;")
# data = cursor.fetchall()
# print(data)

#################################################################################################################################################################

########################################################################
#ADD DATA TO PLAYER_CARDS TABLE 
########################################################################

# with open('Player_cards.csv','r') as csv_file:
#     csv_reader= csv.reader(csv_file)

#     for line in csv_reader:
#         Player_ID = line[0]
#         Yellow_Cards = line[1]
#         Red_Cards = line[2]
#         cursor.execute("INSERT INTO player_cards(Player_ID,Yellow_Cards,Red_Cards) VALUES (%s,%s,%s)",(Player_ID,Yellow_Cards,Red_Cards))
#         mysql.commit()
#     print("Done")





# cursor.execute("SELECT * FROM player_cards;")
# data = cursor.fetchall()
# print(data)





        
################################################################################################################################################################################################

########################################################################
#ADD DATA TO Player_Assists_Goals TABLE 
#########################################################################

with open('Player_Assists_Goals.csv','r') as csv_file:
    csv_reader= csv.reader(csv_file)

    for line in csv_reader:
        Player_ID = line[0]
        No_of_Matches = line[1]
        Goals = line[2]
        Assists = line[3]
        Minutes_played= line[4]
        cursor.execute("INSERT INTO Player_Assist_Goals(Player_ID,No_of_Matches,Goals,Assists,Minutes_played) VALUES (%s,%s,%s,%s,%s)",(Player_ID,No_of_Matches,Goals,Assists,Minutes_played))
        mysql.commit()
    print("Done")





cursor.execute("SELECT * FROM Player_Assist_Goals;")
data = cursor.fetchall()
print(data)
print("Done")

##################################################################################################################################################################################################




