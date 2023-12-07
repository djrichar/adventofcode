def __compute_type__(cards):
    print("cards=", cards)
    jokers = cards.count('J')
    counts = [ count[0] for count in list(set([ (cards.count(c), c) for c in cards if c != 'J']))]
    counts.sort(reverse=True)
    if counts:
        counts[0] += jokers
    if( 5 in counts or jokers == 5):
        return 7
    if( 4 in counts):
        return 6
    if( 3 in counts and 2 in counts):
        return 5
    if( 3 in counts ):
        return 4
    if( 2 == counts.count(2)):
        return 3
    if( 2 in counts):
        return 2
    return 1


class hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = __compute_type__(cards)

    def __repr__(self) -> str:
        return f"{self.cards}, Bid={self.bid}, Type={self.type}\n"

    def _compare(self, other):
        if self.type == other.type:
            for i,c in enumerate(self.cards):
                def card_value(c):
                    return int({"A": 14, "K": 13, "Q":12, "J":1, "T":10}.get(c, c))
                if c != other.cards[i]:
                    return -1 if card_value(c) < card_value(other.cards[i]) else 1
            return 0
        return -1 if self.type < other.type else 1
    
    def __lt__(self, other):
        return self._compare(other) < 0

    def __le__(self, other):
        return self._compare(other) <= 0

    def __eq__(self, other):
        return self._compare(other) == 0

    def __ge__(self, other):
        return self._compare(other) >= 0

    def __gt__(self, other):
        return self._compare(other) > 0

    def __ne__(self, other):
        return self._compare(other) != 0


hands = []
with open('day7-input.txt', 'r') as input:
    hands = [hand(*line.split()) for line in input.readlines()]

hands.sort()
print(hands)
print("hands", sum([ v.bid * (index+1) for index, v in enumerate(hands)]))