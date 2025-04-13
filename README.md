# Python-Assignment-3-2302031800007
# 🏏 IPL Data Analyzer

This mini project is a part of my **Python Programming Assignment (Unit-7)**. It focuses on analyzing IPL cricket data using the **Pandas** library in Python.

## 📌 Project Objective
To explore and analyze IPL match statistics such as:
- Total matches per season
- Team performance over the years
- Player awards
- Toss vs match wins
- Venue popularity
- Batsmen aggression

## 📁 Dataset Used
Two CSV files:
- `matches.csv` – match-level data
- `deliveries.csv` – ball-by-ball data

> Sample dataset includes seasons from 2017–2019 for demo purposes.

## 🛠️ Technologies Used
- Python
- Pandas
- (Optional) Matplotlib / Seaborn for visualization

## 📊 Key Features
- Year-wise IPL champions
- Top teams and players
- Most played venues
- Toss winner vs match winner analysis
- Most sixes by batsmen

## 📄 Output Sample
Total Matches Per Season:
season
2017    2
2018    2
2019    1
Name: count, dtype: int64

Most Wins by Teams:
winner
SRH    1
RPS    1
KKR    1
MI     1
CSK    1
Name: count, dtype: int64

Toss Winner vs Match Winner Count:
Matches where Toss Winner also Won the Match: 2

Top 5 Players with Most 'Player of the Match' Awards:
player_of_match
Yuvraj     1
Smith      1
Russell    1
Rohit      1
Dhoni      1
Name: count, dtype: int64

Venues with Most Matches Hosted:
venue
Rajiv Gandhi Intl    1
MCA Stadium          1
Wankhede             1
Kotla                1
Chepauk              1
Name: count, dtype: int64

Year-wise IPL Champion:
   season winner
0    2017    RPS
1    2018     MI
2    2019    CSK

Most Aggressive Batsmen (Top 3 by 6s):
batsman
Kohli      1
Russell    1
Name: count, dtype: int64
