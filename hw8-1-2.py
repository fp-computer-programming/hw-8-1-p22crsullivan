# Author: CRS 12/09/21
def winner():

team1_wins = input("Please enter how many games team 1 won.")
team1_ties = input("Please enter how many games team 1 tied.")
team2_wins = input("Please enter how many games team 2 won.")
team2_ties = input("Please enter how many games team 2 tied.")
total_points_team1 = int(team1_ties + (team1_wins * 3))
total_points_team2 = int(team2_ties + (team2_wins * 3))
if total_points_team1 > total_points_team2:
    print("Team 1 finished with more points.")
else:
    print("Team 2 finished with more points.")