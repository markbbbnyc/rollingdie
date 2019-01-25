import numpy as np
import pandas as pd
import random
import os
from tabulate import tabulate

# Variables
die_roll = 0
die_type = 6
die_payout = die_type
player_bet = 1
player_win = 0
player_purse = 100
counter = 0
# Keeping track
turn_list = []
purse_list =[]
bet_list = []
win_loss_list = []
rolled_number_list = []
picked_number_list = []
track = {'Turns':turn_list,'Purse':purse_list, 'Bet':bet_list, 'Win_Loss':win_loss_list, 'Rolled_Number':rolled_number_list,
'Picked_Number':picked_number_list}

clear = "\n" * 80
print(clear)
print("\n \n You start with a purse of $100 and play with a", die_type, "sided die \n")

while player_purse > 0:
    counter = counter +1
# Player set bet or quits
    player_bet = int(input("\n How much do you want to bet? You win 500% or lose all. Type '0' to cash out --> "))
    if player_bet == 0:
        print("\n Thank you for playing, here are your $", player_purse)
        break
# Player starts turn and picks winning number
    player_pick = int(input("\n Pick a number from 1 to 6 --> "))
# die roll
    die_roll = random.randint(1,6)
    print("\n You rolled a",die_roll,"\n")
# Player wins
    if player_pick == die_roll:
        player_win = player_bet * die_payout
        player_purse = player_purse + player_win
        print("\n You Win :-) $", player_win, " and have total $", player_purse, "Do you want to quit? \n")
# Player loses
    else:
        player_win = -1 * player_bet
        player_purse = player_purse + player_win
        print("\n You lose, sorry. I take your bet of $", player_bet," and you have $", player_purse, "in your purse. \n ")
# keeping track
    turn_list.append(counter)
    bet_list.append(player_bet)
    rolled_number_list.append(die_roll)
    picked_number_list.append(player_pick)
    win_loss_list.append(player_win)
    purse_list.append(player_purse)
    if player_purse == 0:
        print("\n     Good luck next time. \n ")
        break
# ending the game and results
print("\n \n Thank you for playing. Here are your Results: \n \n ")
print(tabulate(track, headers=['Turn', 'Purse', 'Bet', 'Win/Loss', 'Rolled_Number', 'Picked_Number']))
