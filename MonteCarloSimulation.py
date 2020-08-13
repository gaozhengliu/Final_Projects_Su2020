import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import doctest
import pytest
import typing

def encounter(self):
    picked_dict = {}
    for i in self.zombie_UIN:
        picked_dict[rd.choice(self.survivors_UIN)] = i
    return picked_dict


def attack(self, picked_dict: dict):
    for i in picked_dict.keys():
        attacker = []
        attacker.append(picked_dict[i]) # Avoid the value of the key is typye int when that person only has one zombie to attack
        l = len(attacker)
        index = rd.random()
        fate = 1
        for x in range(l):
            fate = fate * index
        fate = 1 - fate
        if fate > 0.8:
            # That poor person was eaten by zombie(s)
            self.survivors_UIN.remove(i)
            self.survivors_number = self.survivors_number -1
        elif fate > 0.4:
            # That poor person was turned into a new zombie
            self.zombie_UIN.append(i)
            self.survivors_UIN.remove(i)
            self.survivors_number = self.survivors_number - 1
            self.zombies_number = self.zombies_number + 1
        elif fate < 0.1:
            # That brave and lucky person escaped and killed a zombie
            dead_zombie = rd.choice(attacker)
            self.zombie_UIN.remove(dead_zombie)
            self.zombies_number = self.zombies_number - 1
        else:
            # That lucky person escaped
            pass
    self.survivors_number = len(self.survivors_UIN)
    self.zombies_number = len(self.zombie_UIN)

def sensor_passive(self):
    pass

def assign_ammo(self):
    ammo_dict = {}
    if self.ammo < 1:
        return ammo_dict
    ammo_per_person = round(self.ammo/self.survivors_number)
    ammo_std = ammo_per_person * 0.5
    for i in self.survivors_UIN:
        has_ammo = round(rd.normalvariate(ammo_per_person,ammo_std))
        ammo_dict[i] = has_ammo
    return ammo_dict

def defense(self,picked_dict = {}):
    ammo_dict = assign_ammo(self)
    if ammo_dict is None:
        return
    if self.strategy == 2:
        for person in ammo_dict:
            ani = ammo_dict[person]
            if ani > 0:
                for i in range(ani):
                    if self.zombies_number > 0:
                        break
                    shoot_rate = rd.random()
                    if shoot_rate > 0:
                        self.ammo = self.ammo - 1
                        #hit_rate = rd.random()
                        hit_rate = 1
                        if hit_rate > 0.5:
                            uin = rd.choice(self.zombie_UIN)
                            self.zombie_UIN.remove(uin)
                            self.zombies_number = self.zombies_number-1


    if self.strategy == 3:
        pass


def one_day(self):
    if self.ammo>0 and self.strategy > 1:
        defense(self)
    picked_dict = encounter(self)
    attack(self, picked_dict)
    self.day = self.day +1
    #print(len(self.zombie_UIN),len(self.survivors_UIN))
    return self

def one_town(a, b, c, s):
    # One Town Several Days
    t = Town(a, b, c, s)
    while (t.zombies_number * t.survivors_number != 0):
        one_day(t)
    t.end()
    return(t.winner,t.day)

class Town:
    def __init__(self,a=5000,b=10,c=0,s=1):
        self.all_citizens = a
        self.zombies_number = b
        self.survivors_number = a-b
        self.all_citizen_UIN = list(range(a))
        rd.shuffle(self.all_citizen_UIN)
        self.zombie_UIN = self.all_citizen_UIN[0:b]
        self.survivors_UIN = self.all_citizen_UIN[b:a-1]
        self.ammo = c
        self.strategy = s
        self.day = 0
        self.winner = 0

    def end(self):
        if len(self.zombie_UIN) <=0:
            self.winner = 1
            self.close()
        if len(self.survivors_UIN) <= 0:
            self.winner = -1
            self.close()
    def close(self):
        pass

if __name__ == '__main__':
    # Several Town
    a = 5000 # number of citizen
    b = 50 # number of initial zombie
    c = 10000 # ammo
    s = 2 #strategy

    winners = []
    days = []
    runs = 500
    for i in range(runs):
        winner, day = one_town(a, b, c, s)
        winners.append(winner)
        days.append(day)
    ind = range(1,runs+1)


    win = pd.DataFrame({'Index' :range(1,runs+1),'Winner' : winners, 'Days' :days})

    win_compare = win[['Winner','Days']].groupby('Winner').count().reset_index()
    print(win_compare)
    win_human = win[win.Winner == 1]
    ave_human_win_days = win_human['Days'].mean()
    print(win_human)
    print(ave_human_win_days)
    win_zombie = win[win.Winner == -1]
    ave_zombie_win_days = win_zombie['Days'].mean()
    print(win_zombie)
    print(ave_zombie_win_days)

    win_human_days = win_human[['Days']].groupby('Days').count().reset_index()
    #plt.plot()
    '''
    #plt.plot(days)
    #plt.ylabel('days')
    days_dict = {}
    for i in days:
        if i in days_dict.keys():
            days_dict[i] = days_dict[i] +1
        else:
            days_dict[i] = 1
    sorted_day = sorted(days_dict.items())
    days = []
    values = []
    for item in sorted_day:
        days.append(item[0])
        values.append(item[1])
    plt.plot(days,values)
    plt.show()
    '''
