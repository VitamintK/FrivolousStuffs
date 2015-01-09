import json
from collections import defaultdict


def currentPlayers():
    playerson = json.load(open("players.json"))
    players = [player for player in playerson]
    firstnames = defaultdict(set)
    for player in players:
        playerspl = player.split(' ')
        firstnames[playerspl[0]].add(playerspl[-1])
    return firstnames
    
def allPlayers():
    firstnames = defaultdict(set)
    playertext = open("playertext.txt")
    for player in playertext:
        player = player.strip()
        playerspl = player.split(',')
        if len(playerspl) > 1:
            firstnames[playerspl[1].split()[0]].add(playerspl[0].split()[-1])
    return firstnames
        
firstnames = allPlayers()
cache = dict()

def getnext(prevlastname, namessofar):
    namessofar = namessofar[:]
    if prevlastname in cache:
        return cache[prevlastname]
    
    if prevlastname in firstnames:
        lastnamecandidates = []
        for lastname in firstnames[prevlastname]:
            if (prevlastname, lastname) not in namessofar:
                if lastname in cache:
                    lastnamecandidates.append([(prevlastname, lastname)] + cache[lastname])
                else:
                    lastnamecandidates.append(
                        getnext(lastname, namessofar[:] + [(prevlastname, lastname)]))
        greatestcand = max(lastnamecandidates, key = lambda x: len(x))
        #cache[prevlastname] = greatestcand
        return greatestcand
            

    else:
        return namessofar

def formatName(name):
    return ' '.join([n[0] for n in name] + [name[-1][1]])

starters = []
for firstname, lastnames in firstnames.items():
#[('Paul', {'George'})]:#firstnames.items():
    for lastname in lastnames:
        #print(getnext(lastname, [(firstname, lastname)]))
        name = getnext(lastname, [(firstname, lastname)])
        if len(name) > 1:
            print(formatName(name))
        starters.append(name)
        
print(max(starters, key = lambda x: len(x)))
print(formatName(max(starters, key = lambda x: len(x))))
print(sorted(cache.items(), key = lambda x: len(x[1])))

