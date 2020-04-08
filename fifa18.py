# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:48:11 2020

@author: utsav
"""


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("E:\\Practice\\fifa-18-demo-player-dataset\\PlayerPlayingPositionData.csv")
df_1 = pd.read_csv("E:\\Practice\\fifa-18-demo-player-dataset\\PlayerPersonalData.csv")
df_2 = pd.read_csv("E:\\Practice\\fifa-18-demo-player-dataset\\PlayerAttributeData.csv")
df_3 = pd.read_csv("E:\\Practice\\fifa-18-demo-player-dataset\\CompleteDataset.csv")
df.info()
df.columns
df.shape

df

df_1.columns
df_2.columns
df_3.columns


spanish_players = df_3[df_3["Nationality"] == "Spain"]
"Players with overall greater than 80"
spanish_players[spanish_players["Overall"]> 85]["Name"]

eng_players = df_3[df_3["Nationality"] == "England"]
eng_players[eng_players["Potential"] > 80]["Name"]

chelsea_players = df_3[df_3["Club"] == 'Chelsea']
print(chelsea_players.shape)

filtered = df_3[df_3["Overall"]> 85]
print(filtered)
filt_by_club = filtered.groupby("Club")[["Name","Age",]].mean()
filt_by_club.plot(kind = "bar", color = 'rgbkymc')


plt.style.use('fivethirtyeight')

""" Players with overall greater than 85 playing for a country"""
def country_nation(*country):
    players = df_3[df_3["Nationality"].isin(country)][["Name","Age","Potential","Overall","Club"]]
    players = players[players["Overall"]> 85]
    return players,"\n", players.shape
country_nation("France","Spain","Belgium","Germany")


""" Analyzing Clubs"""

def club(*club):
    club_players = df_3[df_3["Club"].isin(club)][["Name","Age","Overall", "Potential","Nationality"]]
    club_players = club_players[club_players["Overall"] > 80]
    return club_players

club("Chelsea","Arsenal")

london =  ["Chelsea","Arsenal"]
for london_clubs in london:
    print(club(london_clubs))

x = club("Liverpool")
print(x)
x.shape
import seaborn as sns

""" Is Data Normally Distributed"""
plt.figure(figsize = (12,6))
sns.distplot(df_3["Overall"])
df_3["Overall"].mean()
df_3["Overall"].mode()
df_3["Overall"].median()


pearsoncorr = df_3.corr(method='pearson')
pearsoncorr
sns.lineplot(x = df_3["Overall"], y = df_3["Age"] , data = df_3)


df_3["Wage"] = df_3["Wage"].str.replace("K","").str.replace("€","")
df_3["Wage"] = df_3["Wage"].astype(int)
df_3["Wage"].dtype


df_3.groupby("Age")[["Age", "Wage"]].mean().plot(kind = "bar", x ="Age",y = "Wage")

filtered["Wage"] = filtered["Wage"].str.replace("K","").str.replace("€","")
filtered["Wage"] = filtered["Wage"].astype(int)
filtered["Wage"].dtype

wage_per_club = filtered.groupby("Club")["Wage"].mean()
wage_per_club = wage_per_club.plot(kind = "bar")


""" Age """
sns.set(style ="dark", palette="colorblind", color_codes=True)
x = df_3.Age
plt.figure(figsize=(12,8))
ax = sns.distplot(x, bins = 58, kde = False, color='g')
ax.set_xlabel(xlabel="Player\'s age", fontsize=16)
ax.set_ylabel(ylabel='Number of players', fontsize=16)
ax.set_title(label='Histogram of players age', fontsize=20)
plt.show()


""" Eldest Players"""
df_3.columns
eldest = df_3.sort_values("Age", ascending = False)[["Name","Nationality","Club","Age","Overall"]].head(5)
eldest.set_index("Name", inplace =True)

print(eldest)


""" Some CLubs"""
some_clubs = ('Juventus', 'Real Madrid', 'Paris Saint-Germain', 'FC Barcelona', 'Chelsea', 'Manchester United')
clubs = df_3.loc[df_3['Club'].isin(some_clubs)][["Age","Overall","Club"]]
print(clubs)
ax = sns.barplot(x=clubs['Club'], y=clubs['Overall'], palette="rocket")
d = clubs.groupby("Club")["Overall"].mean()
print(d)
ax.set_title(label='Distribution overall in several clubs', fontsize=20)


