#added test comment
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd
import random
import os
from tabulate import tabulate
#np.set_printoptions(threshold=np.nan)
#%matplotlib inline


# Variables

die_roll = 0
die_type = 6
die_payout = die_type
player_bet = 0
player_pick = 0
player_win = 0
player_purse = 100
round = 0
counter = 0


# Keeping track and initialize lists

#turn_list.clear()
#purse_list.clear()
#bet_list.clear()
#win_loss_list.clear()
#rolled_number_list.clear()
#picked_number_list.clear()

round_list = [0]
turn_list = [0]
purse_list =[100]
bet_list = [0]
win_loss_list = [0]
rolled_number_list = [0]
picked_number_list = [0]

track = {'Round':round_list,'Turns':turn_list,'Purse':purse_list, 'Bet':bet_list, 'Win_Loss':win_loss_list, 'Rolled_Number':rolled_number_list,
'Picked_Number':picked_number_list}

for j in range(100):
    round = round +1
    counter = 0
    player_purse = 100

    while player_purse > 0:
        round_list.append(round)
        counter = counter +1
        turn_list.append(counter)
        die_roll = random.randint(1,6)
        rolled_number_list.append(die_roll)
        player_bet = random.randint(0,player_purse)
        bet_list.append(player_bet)
        player_pick = random.randint(1,6)
        picked_number_list.append(player_pick)
        if player_pick == die_roll:
            player_win = player_bet * die_payout
        else:
            player_win = -1 * player_bet
        win_loss_list.append(player_win)
        player_purse = player_purse + player_win
        purse_list.append(player_purse)
        if player_purse == 0:
            break

header = track.keys()
#print(tabulate(track, headers=['Turn', 'Purse', 'Bet', 'Win/Loss', 'Rolled_Number', 'Picked_Number']))
#print(tabulate(track, headers=header))

df = pd.DataFrame.from_dict(track)


x = df["Round"].unique()
y1 = df.groupby("Round")["Bet"].max()
y2 = df.groupby("Round")["Purse"].max()
y3 = df.groupby("Round")["Turns"].max()

f = plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.bar(x,y1)
plt.title("This is how it went down")
plt.ylabel("Maximum Bet")

plt.subplot(3,1,2)
plt.bar(x,y2)
plt.ylabel("Maximum Purse")
plt.xlabel("Rounds")

plt.subplot(3,1,3)
plt.bar(x,y3)
plt.ylabel("Games per Round")
plt.xlabel("Rounds")

plt.show()
