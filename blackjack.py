"""blackjack.py: in which I do various blackjack related things."""
import itertools
import numpy
import random

deck=[]
for i in xrange(1,14):
    if i<10:
        deck+=[i]*4
    else:
        deck+=[10]*4
average_card_value = float(sum(deck))/len(deck) #ignoring aces' ability to be 11

def simulate_custom_shoe(shoe=[average_card_value]):
    """simulation where the shoe is comprised solely of a magical card
    with value 6.53... (average_card_value [with aces as 1])"""
    uniques=set(deck)
    for i in itertools.combinations(uniques,2):
        for upcard in uniques:
            play_round()

def basic_trainer():
    """quick basic trainer"""
    hard = ['17\x9620', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
['16', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'SU', 'SU', 'SU']
['15', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'SU', 'H']
['13\x9614', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
['12', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
['11', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'H']
['10', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'Dh', 'H', 'H']
['9', 'H', 'Dh', 'Dh', 'Dh', 'Dh', 'H', 'H', 'H', 'H', 'H']
['5\x968', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
    while True:
        upcard,urcarda,urcardb = random.randint(1,11),random.randint(1,11),random.randint(1,11)
        print "dealer's upcard: {0}".format(str(upcard))
        print "your cards: {0} and {1}".format(str(urcarda),str(urcardb))
        while upcarda+upcardb<
          
