import collections
Card = collections.namedtuple('card',['rank','suit'])
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards=[Card(rank,suit) for rank in self.ranks
                                    for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):#把[]操作交给self._cards列表
        return self._cards[position]

beer_card=Card('7','diamonds')
print(beer_card)
deck=FrenchDeck()
# print(len(deck))
print(deck[:4])
for card in deck:#doctest:+ELLIPSIS
    print(card)