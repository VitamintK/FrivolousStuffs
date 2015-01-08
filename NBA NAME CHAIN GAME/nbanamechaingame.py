import json

playerson = json.load(open("players.json"))

players = [player for player in playerson]
print(players[:100])
    
