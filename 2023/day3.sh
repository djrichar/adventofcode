#!/bin/python3
import math
import os
import random
import re
import sys

def tonumber(line, y):
    if y >= 0 and y < len(line) and line[y].isdigit():
        begin_index = next((i+1 for i, c in reversed(list(enumerate(line[:y]))) if not c.isdigit()), 0)
        end_index = next((y+i for i, c in list(enumerate(line[y:])) if not c.isdigit()), len(line))
        return int("".join(line[begin_index:end_index]))
    return 0
    
def find_adjacents(schematic, x, y):
    adjacents = []
    # before
    # x(x-1,y-1) x(x-1,y) x(x-1,y+1)
    # x    x     x
    # x    x     x
    adjacents.append(tonumber(schematic[x], y-1))
    adjacents.append(tonumber(schematic[x], y+1))
    if x > 0 :
        n1 = tonumber(schematic[x-1], y-1)
        n2 = tonumber(schematic[x-1], y)
        n3 = tonumber(schematic[x-1], y+1)
        adjacents.append(n1)
        if n1 != n2:
            adjacents.append(n2)
        if n2 != n3:
            adjacents.append(n3)
    if x < len(schematic)-1:
        n1 = tonumber(schematic[x+1], y-1)
        n2 = tonumber(schematic[x+1], y)
        n3 = tonumber(schematic[x+1], y+1)
        adjacents.append(n1)
        if n1 != n2:
            adjacents.append(n2)
        if n2 != n3:
            adjacents.append(n3)
    return adjacents
            
schematic = []
with open('day3-input.txt', 'r') as input:
    for line in input.readlines():
        schematic.append(list(line[:-1]))

numbers=[]    
gears = []   
for x, line in enumerate(schematic):
    for y in [y for y, c in enumerate(line) if ord(c) < 65 and c not in ".0123456789"]:
        d = [ n for n in find_adjacents(schematic, x, y) if n > 0 ]
        if line[y] == '*' and len(d) == 2:
            gears.append(d[0]*d[1])
        print("result: x=",x, "y=", y, d)
        numbers += d
    
print(sum(numbers))
print(sum(gears))
# print(sum(game.power() for game in games))
