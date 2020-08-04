import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import doctest
import pytest
import typing

class Zombie:
    sensor_human = rd.random() # Random float:  0.0 <= x < 1.0




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
        elif fate > 0.4:
            # That poor person was turned into a new zombie
            self.zombie_UIN.append(i)
            self.survivors_UIN.remove(i)
        elif fate < 0.1:
            # That brave and lucky person escaped and killed a zombie
            dead_zombie = rd.choice(attacker)
            self.zombie_UIN.remove(dead_zombie)
        else:
            # That lucky person escaped
            pass
    self.survivors_number = len(self.survivors_UIN)
    self.zombies_number = len(self.zombie_UIN)

def sensor_passive(self):
    pass

def defense(self):
    pass


def one_day(self):
    picked_dict = encounter(self)
    attack(self, picked_dict)
    self.day = self.day +1
    return self

def one_town():
    # One Town Several Days
    a: int = 500
    b: int = 50
    c: int = 1000
    #t = Town(a, b)
    t = Town(a, b, c)
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
    for i in range(500):
        winner, day =one_town()
        winners.append(winner)
        days.append(day)
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