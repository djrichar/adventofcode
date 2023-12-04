#!/bin/python3
import math
import os
import random
import re
import sys

results = []
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]
forward = re.compile(r'(\d|%s)' % "|".join(numbers) )
reverse = re.compile(r'(\d|%s)' % "|".join([ n[::-1] for n in numbers]) )
with open('day1-input.txt', 'r') as input:
    for line in input.readlines():
        d1 = forward.search(line)
        d2 = reverse.search(line[::-1])
        if d1 and d2:
            i1 = d1.group(0)
            if i1 in numbers:
                i1 = str(numbers.index(i1))
            i2 = d2.group(0)
            if i2[::-1] in numbers:
                i2 = str(numbers.index(i2[::-1]))
            print(i1, i2, line)
            results.append(int(i1 + i2))
print(sum(results))