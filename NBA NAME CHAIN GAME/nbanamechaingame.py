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
        if len(player) > 1:
            try:
                firstnames[playerspl[1].split()[0]].add(playerspl[0].split()[-1])
            except:
                print(player)
    return firstnames
        
firstnames = allPlayers()
print(firstnames['Michael'])
