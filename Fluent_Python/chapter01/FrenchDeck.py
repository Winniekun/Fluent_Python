'''
@author：KongWeiKun
@file: FrenchDeck.py
@time: 17-10-18 上午10:07
@contact: 836242657@qq.com
'''
import  collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards=[Card(rank,suit) for rank in self.ranks
                                     for suit in self.suits]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, postion):
        return self._cards[postion]


beer_card=Card('7','diamonds')
print(beer_card)
deck=FrenchDeck()
print(len(deck))
print(deck[-1])
s=Card('Q','fsfas') in deck
m=Card('Q','hearts') in deck
print(m)