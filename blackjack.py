"""blackjack.py: in which I do various blackjack related things."""
import itertools
import numpy

deck=[]
for i in xrange(1,14):
    if i<10:
        deck+=[i]*4
    else:
        deck+=[10]*4
average_card_value = float(sum(deck))/len(deck) #ignoring aces' ability to be 11

def simulate_sixes():
    """simulation where the shoe is comprised solely of a magical card
    with value 6.53... (average_card_value [with aces as 1])"""
    uniques=set(deck)
    for i in itertools.combinations(uniques,2):
        for upcard in uniques:
            play_round()
            
            
