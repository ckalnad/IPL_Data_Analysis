# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sqlite3
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

path = "C:/Users/ckaln/Desktop/"
database = path + 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)

#print(tables)

print("DONE")
detailed_matches = pd.read_sql("""SELECT DISTINCT(Match.Match_Id), Match.Team_1, Match.Team_2, Match.Match_Date, Match.Season_Id, Match.Venue_Id, Match.Toss_Winner, Match.Toss_Decide,
                                Match.Win_Type, Match.Win_Margin, Match.Outcome_type, Match.Match_Winner, Match.Man_of_the_Match, Team.Team_Name, Toss_Decision.Toss_Name,
                                Win_By.Win_Type, Venue.Venue_Name, City.City_Name, Country.Country_Name
                                FROM Match
                                JOIN Team on Team.Team_Id = Match.Match_Winner
                                JOIN Toss_Decision on Toss_Decision.Toss_Id = Match.Toss_Decide
                                JOIN Win_By on Win_By.Win_Id = Match.Win_Type
                                JOIN Venue on Venue.Venue_Id = Match.Venue_Id
                                JOIN City on City.City_Id = Venue.City_Id
                                JOIN Country on Country.Country_Id = City.Country_Id
                                ;""", conn)

detailed_matches.to_excel("IPL_match.xlsx")  

print("DONE")
Man_of_the_match = pd.read_sql("""SELECT DISTINCT(Match.Match_Id), Match.Team_1, Match.Team_2, Match.Match_Date, Match.Season_Id, Match.Venue_Id, Match.Toss_Winner, Match.Toss_Decide,
                                Match.Win_Type, Match.Win_Margin, Match.Outcome_type, Match.Match_Winner, Match.Man_of_the_Match, Team.Team_Name, Toss_Decision.Toss_Name,
                                Win_By.Win_Type, Venue.Venue_Name, City.City_Name, Country.Country_Name, Player.Player_Name, Player.Batting_hand, Player.Bowling_skill,
                                Batting_Style.Batting_hand, Bowling_Style.Bowling_skill
                                FROM Match
                                JOIN Team on Team.Team_Id = Match.Match_Winner
                                JOIN Toss_Decision on Toss_Decision.Toss_Id = Match.Toss_Decide
                                JOIN Win_By on Win_By.Win_Id = Match.Win_Type
                                JOIN Venue on Venue.Venue_Id = Match.Venue_Id
                                JOIN City on City.City_Id = Venue.City_Id
                                JOIN Country on Country.Country_Id = City.Country_Id
                                JOIN Player on Player_Id = Match.Man_of_the_Match
                                JOIN Batting_Style on Batting_Id = Player.Batting_hand
                                JOIN Bowling_Style on Bowling_ID = Player.Bowling_skill
                                ;""", conn)

Man_of_the_match.to_excel("IPL_MOM.xlsx")

Ball_by_Ball = pd.read_sql("""SELECT DISTINCT(Ball_by_Ball.Match_Id), Ball_by_Ball.Over_Id, Ball_by_Ball.Ball_Id, Ball_by_Ball.Innings_No, Ball_by_Ball.Team_Batting,
                            Ball_by_Ball.Team_Bowling, Ball_by_Ball.Striker_Batting_Position, Ball_by_Ball.Striker, Ball_by_Ball.Non_Striker, Ball_by_Ball.Bowler,
                            Extra_Runs.Extra_Type_Id, Extra_Runs.Extra_Runs, Extra_Type.Extra_Name, Batsman_Scored.Runs_Scored, Wicket_taken.Player_Out,
                            Wicket_taken.Kind_Out, Wicket_taken.Fielders, Out_Type.Out_Name, Player.Player_Name, Player.Batting_hand, Batting_Style.Batting_hand,
                            Team.Team_Name
                            FROM Ball_by_Ball
                            LEFT JOIN Extra_Runs on Extra_Runs.Match_Id = Ball_by_Ball.Match_Id 
                            AND Extra_Runs.Over_Id = Ball_by_Ball.Over_Id
                            AND Extra_Runs.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Extra_Runs.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Extra_Type on Extra_Type.Extra_Id = Extra_Runs.Extra_Type_Id 
                            LEFT JOIN Batsman_Scored on Batsman_Scored.Match_Id = Ball_by_Ball.Match_Id 
                            AND Batsman_Scored.Over_Id = Ball_by_Ball.Over_Id
                            AND Batsman_Scored.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Batsman_Scored.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Wicket_Taken on Wicket_Taken.Match_Id = Ball_by_Ball.Match_Id 
                            AND Wicket_Taken.Over_Id = Ball_by_Ball.Over_Id
                            AND Wicket_Taken.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Wicket_Taken.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Out_Type on Out_Type.Out_Id = Wicket_Taken.Kind_Out
                            JOIN Player on Player.Player_Id = Ball_by_Ball.Striker
                            JOIN Batting_Style on Batting_Style.Batting_Id = Player.Batting_hand
                            JOIN Team on Team.Team_Id = Ball_by_Ball.Team_Batting
                            ;""", conn)

Ball_by_Ball.to_excel("IPL_Ball_by_Ball.xlsx") 

print("DONE")

Ball_by_Ball_2 = pd.read_sql("""SELECT DISTINCT(Ball_by_Ball.Match_Id), Ball_by_Ball.Over_Id, Ball_by_Ball.Ball_Id, Ball_by_Ball.Innings_No, Ball_by_Ball.Team_Batting,
                            Ball_by_Ball.Team_Bowling, Ball_by_Ball.Striker_Batting_Position, Ball_by_Ball.Striker, Ball_by_Ball.Non_Striker, Ball_by_Ball.Bowler,
                            Extra_Runs.Extra_Type_Id, Extra_Runs.Extra_Runs, Extra_Type.Extra_Name, Batsman_Scored.Runs_Scored, Wicket_taken.Player_Out,
                            Wicket_taken.Kind_Out, Wicket_taken.Fielders, Out_Type.Out_Name, Player.Player_Name, Player.Bowling_skill, Bowling_Style.Bowling_skill,
                            Team.Team_Name
                            FROM Ball_by_Ball
                            LEFT JOIN Extra_Runs on Extra_Runs.Match_Id = Ball_by_Ball.Match_Id 
                            AND Extra_Runs.Over_Id = Ball_by_Ball.Over_Id
                            AND Extra_Runs.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Extra_Runs.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Extra_Type on Extra_Type.Extra_Id = Extra_Runs.Extra_Type_Id 
                            LEFT JOIN Batsman_Scored on Batsman_Scored.Match_Id = Ball_by_Ball.Match_Id 
                            AND Batsman_Scored.Over_Id = Ball_by_Ball.Over_Id
                            AND Batsman_Scored.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Batsman_Scored.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Wicket_Taken on Wicket_Taken.Match_Id = Ball_by_Ball.Match_Id 
                            AND Wicket_Taken.Over_Id = Ball_by_Ball.Over_Id
                            AND Wicket_Taken.Ball_Id = Ball_by_Ball.Ball_Id
                            AND Wicket_Taken.Innings_No = Ball_by_Ball.Innings_No
                            LEFT JOIN Out_Type on Out_Type.Out_Id = Wicket_Taken.Kind_Out
                            JOIN Player on Player.Player_Id = Ball_by_Ball.Bowler
                            JOIN Bowling_Style on Bowling_Style.Bowling_Id = Player.Bowling_skill
                            JOIN Team on Team.Team_Id = Ball_by_Ball.Team_Bowling
                            ;""", conn)

Ball_by_Ball_2.to_excel("IPL_Ball_by_Ball_2.xlsx") 

print("DONE")

