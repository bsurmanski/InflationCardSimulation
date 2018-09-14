import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
names = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']

class Card(object):
    def __init__(self, value, name):
		self.value = value
		self.name = name
    
    def __repr__(self):
        return self.name
    
    def __cmp__(self, o):
        return o.value - self.value

class Strategy(object):
    
    def set_hand(self, cards):
        self.cards = cards
    
    def set_context(self, context):
        self.context = context
    
    def act(self):
        return None
    
    def add_card(self, card):
        self.cards.append(card)
    
    def __repr__(self):
        st = type(self).__name__ + ': '
        for card in self.cards:
            st += str(card)
        return st

class Context(object):
    def __init__(self):
        self.players = []
    
    def add_player(self, strategy):
        self.players.append(strategy)
        
    def do_turn():
        cards = []
        for player in self.players:
            card = player.act()
            if card:
                cards.append(card)
            cards.sort()
        for i, card in enumerate(cards):
            
    
    def __repr__(self):
        st = ''
        for player in self.players:
            st += str(player) + '\n'
        return st

def random_deck():
    deck = []
    for v,n in zip(values * 4, names * 4):
        deck.append(Card(v, n))
    random.shuffle(deck)
    random.shuffle(deck)
    return deck

def deal(nplayers):
    deck = random_deck()
    hands = []
    for i in range(0, nplayers):
        hands.append([])
    for i, card in enumerate(deck):
        hands[i%nplayers].append(card)
    return hands


def main():
    c = Context()
    strats = [LowestStrategy(), HighestStrategy()]
    for strat, hand in zip(strats, deal(len(strats))):
        print len(hand)
        strat.set_hand(hand)
        strat.set_context(c)
        c.add_player(strat)
    print c

class LowestStrategy(Strategy):
    
    def act(self):
        self.cards = sorted(self.cards, reverse=True)
        return self.cards.pop()
        
class HighestStrategy(Strategy):
    
    def act(self):
        self.cards = sorted(self.cards)
        return self.cards.pop()
        
if __name__ == '__main__':
    main()