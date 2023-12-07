
class hand:
    def __init__(self, cards, bid, **v):
        self.cards = cards
        self.bid = int(bid)
        self.cardcount = dict((c, cards.count(c)) for c in cards)
        self.with_joker = v.get('joker', False)
        self.type = self.__compute_type__()
        

    def __compute_type__(self):
        counts = [ v for k, v in self.cardcount.items() if not (self.with_joker and k=='J')]
        counts.sort(reverse=True)
        if self.with_joker:
            if not counts: counts.append(0)
            counts[0] += self.cardcount.get("J", 0)
        if( 5 in counts):
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

    def __repr__(self) -> str:
        return f"{self.cards}, Bid={self.bid}, Type={self.type}, {self.cardcount}\n"

    def _compare(self, other):
        if self.type == other.type:
            for i,c in enumerate(self.cards):
                def card_value(c):
                    return int({"A": 14, "K": 13, "Q":12, "J": 1 if self.with_joker else 11, "T":10}.get(c, c))
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
hands2 = []
with open('day7-input.txt', 'r') as input:
    for line in input.readlines():
        hands.append(hand(*line.split()))
        hands2.append(hand(*line.split(),joker=True))
hands.sort()
print("hands", sum([ v.bid * (index+1) for index, v in enumerate(hands)]))
hands2.sort()
print("hands2", sum([ v.bid * (index+1) for index, v in enumerate(hands2)]))