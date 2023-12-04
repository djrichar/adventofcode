#!/bin/python3
import math
import os
import random
import re
import sys

numbers = {
    "zero": "0o",
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "4",
    "five": "5e",
    "six": "6",
    "seven": "7n",
    "eight": "e8t",
    "nine": "n9e"
}

forward1 = re.compile(r'\d')
reverse1 = re.compile(r'\d')

def problem1(line):
    d1 = forward1.search(line)
    d2 = reverse1.search(line[::-1])
    return int(d1.group(0) + d2.group(0)) if d1 and d2 else 0

def problem2(line):
    for key, value in numbers.items():
        line = line.replace(key, value)
    return problem1(line)

result1=[]
result2=[]
with open('day1-input.txt', 'r') as input:
    for line in input.readlines():
        result1.append(problem1(line))
        result2.append(problem2(line))
print(sum(result1))
print(sum(result2))