import pandas as pd

# Load data
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("Data Loaded Successfully!")

# Total matches per season
print("\nTotal Matches Per Season:")
print(matches['season'].value_counts().sort_index())

# Most wins by team
print("\nMost Wins by Teams:")
print(matches['winner'].value_counts())

# Toss Winner vs Match Winner
print("\nToss Winner vs Match Winner Count:")
same_winner = matches[matches['toss_winner'] == matches['winner']]
print(f"Matches where Toss Winner also Won the Match: {len(same_winner)}")

# Top 5 Player of the Match
print("\nTop 5 Players with Most 'Player of the Match' Awards:")
print(matches['player_of_match'].value_counts().head(5))

# Venues with most matches
print("\nVenues with Most Matches Hosted:")
print(matches['venue'].value_counts().head(5))

# Year-wise IPL Champion (winner of last match of each season)
print("\nYear-wise IPL Champion:")

# Fix: Avoid deprecated groupby().apply() behavior
matches_sorted = matches.sort_values(['season', 'id'])
last_matches = matches_sorted.groupby('season').tail(1)
champions = last_matches[['season', 'winner']].reset_index(drop=True)

print(champions)

# Most aggressive batsman (max 6s in deliveries)
print("\nMost Aggressive Batsmen (Top 3 by 6s):")
sixes = deliveries[deliveries['runs'] == 6]
top_six_hitters = sixes['batsman'].value_counts().head(3)
print(top_six_hitters)
