#!/bin/python3
import math
import os
import random
import re
import sys

class Game:
    def __init__(self, number):
        self.number = int(number)
        self.red = []
        self.blue = []
        self.green = []
    
    def add_set(self, set):
        for color in set.split(','):
            self.add_color(*color.strip().split(' '))
    
    def add_color(self, number, color):
        getattr(self, color).append(int(number))

    def possible(self):
        return not (
            next((x for x in self.red if x > 12), None) or 
            next((x for x in self.green if x > 13), None) or 
            next((x for x in self.blue if x > 14), None))
    
    def power(self):
        return max(self.red) * max(self.green) * max(self.blue)

    def __repr__(self) -> str:
        return "%s red:%s, green:%s, blue:%s\n" % (self.number, self.red, self.green, self.blue)

games = []
with open('day2-input.txt', 'r') as input:
    for line in input.readlines():
        gameIndex, sets = line.split(':')
        print(gameIndex, sets)
        game = Game(gameIndex[5:])
        for set in sets.split(';'):
            game.add_set(set)
        games.append(game)

print(games)
print(sum(game.power() for game in games))
