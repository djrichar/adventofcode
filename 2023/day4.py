import re

class Card:
    def __init__(self, index, winners):
        self.index = index
        self.winners = winners
        self.duplicates = 0


scorecards=[]
with open('day4-input.txt', 'r') as input:
    for line in input.readlines():
        data = re.split(r'[|:]', line)
        index = int(data[0][4:].strip())
        scorecards.append(Card(index, list(set(data[1].split()) & set(data[2].split()))))
score = 0
for i, card in enumerate(scorecards):
    if card.winners:
        for l in range(len(card.winners)):
            scorecards[i+1+l].duplicates += 1+card.duplicates
    print(len(card.winners), card.duplicates, card.winners)
    score += card.duplicates + 1
print(score)