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

def assign_animo(self):
    animo_dict = {}
    if self.animo < 1:
        return animo_dict
    animo_per_person = round(self.animo/self.survivors_number)
    animo_std = animo_per_person * 0.5
    for i in self.survivors_UIN:
        has_animo = round(rd.normalvariate(animo_per_person,animo_std))
        animo_dict[i] = has_animo
    return animo_dict

def defense(self,picked_dict = {}):
    animo_dict = assign_animo(self)
    if animo_dict is None:
        return
    if self.strategy == 1:
        for person in animo_dict:
            ani = animo_dict[person]
            if ani > 0:
                for i in range(ani):
                    if self.zombies_number > 0:
                        break
                    shoot_rate = rd.random()
                    if shoot_rate > 0.3:
                        self.animo = self.animo - 1
                        hit_rate = rd.random()
                        if hit_rate > 0.5:
                            uin = rd.choice(self.zombie_UIN)
                            self.zombie_UIN.remove(uin)
                            self.zombies_number = self.zombies_number-1


    if self.strategy == 2:
        pass


def one_day(self):
    if self.animo>0 and self.strategy > 0:
        defense(self)
    picked_dict = encounter(self)
    attack(self, picked_dict)
    self.day = self.day +1
    return self

def one_town():
    # One Town Several Days
    a: int = 500
    b: int = 50
    c: int = 1000
    s: int = 1
    #t = Town(a, b)
    t = Town(a, b, c, s)
    while (t.zombies_number * t.survivors_number != 0):
        one_day(t)
    t.end()
    return(t.winner,t.day)

class Town:
    def __init__(self,a=500,b=50,c=0,s=0):
        self.all_citizens = a
        self.zombies_number = b
        self.survivors_number = a-b
        self.all_citizen_UIN = list(range(a))
        rd.shuffle(self.all_citizen_UIN)
        self.zombie_UIN = self.all_citizen_UIN[0:b]
        self.survivors_UIN = self.all_citizen_UIN[b:a-1]
        self.animo = c
        self.strategy = s
        self.day = 0
        self.winner = 0

    def end(self):
        if len(self.zombie_UIN) ==0:
            self.winner = 1 #how to trans it outside ???
            self.close()
        if len(self.survivors_UIN) == 0:
            self.winner = -1
            self.close()
    def close(self):
        pass

if __name__ == '__main__':
    # Several Town
    winners = []
    days = []
    runs = 500
    for i in range(runs):
        winner, day =one_town()
        winners.append(winner)
        days.append(day)
    ind = range(1,runs+1)

    win = pd.DataFrame({'index' :range(1,runs+1),'winner' : winners, 'days' :days})

    b = 1 in pd.Series(win['winner'])
    print(b)

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
