"""i'm bored af and it's 4:01 am and I can't come up with anything to do
so here's a random word.  I think google captchas have something like this but better.
It's pretty fun to just try to pronounce random words.
next step: programmatically create a random language.  start with allowable letters/phofhuneomes,"""
consonants = list('bcdfghjklmnprstvwxyz') #q
cons_sounds = consonants*15 + [consonant + 'r' for consonant in consonants] + ['thr', 'th', 'ph', 'phr', 'st', 'str', 'pl', 'bl', 'cl', 'fl', 'sl', 'sh', 'sch', 'ch', 'chr', 'schr', 'shr']
vowels = list('aeiou') #y
vowel_sounds = vowels * 10 + [vowel + vowel2 for vowel in vowels for vowel2 in vowels]

import random
def make_word(word_length):
    x = min(random.randint(0,3), 1)
    word = ''
    for i in range(word_length):
        if x:
            word = word + random.choice(vowel_sounds)
        else:
            word = word + random.choice(cons_sounds)
        x = not x
    print(word)

while input('') != 'q':
    word_length = random.randint(2,10)
    make_word(word_length)
"""qriavodrefehruqryu
>>> ================================ RESTART ================================
>>> 
threthryafiqri
>>> ================================ RESTART ================================
>>> 
phyylofriyixro
>>> ================================ RESTART ================================
>>> 
ydiebrophicr
>>> ================================ RESTART ================================
>>> 
wefasrukupr
>>> ================================ RESTART ================================
>>> 
ocegeecacribo
>>> ================================ RESTART ================================
>>> 
lrayreyriexrethea
>>> ================================ RESTART ================================
>>> 
thriedr
>>> ================================ RESTART ================================
>>> 
onrofrir
>>> ================================ RESTART ================================
>>> 
pajr
>>> ================================ RESTART ================================
>>> 
griixriuvra
>>> ================================ RESTART ================================
>>> 
ethagragreno
>>> ================================ RESTART ================================
>>> 
iiyohr
>>> ================================ RESTART ================================
>>> 
dixocruxiw
>>> ================================ RESTART ================================
>>> 
mrievreb
>>> ================================ RESTART ================================
>>> 
aupredeu
>>> ================================ RESTART ================================
>>> 
eaxufuico
>>> ================================ RESTART ================================
>>> 
ugazazeraaz
>>> ================================ RESTART ================================
>>> 
asa
>>> ================================ RESTART ================================
>>> 
ox
>>> ================================ RESTART ================================
>>> 
ozimuimiaj"""
#standalone
