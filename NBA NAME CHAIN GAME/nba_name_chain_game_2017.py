import nba_py.player

players = nba_py.player.PlayerList().info().DISPLAY_LAST_COMMA_FIRST
p = players.str.split(',').apply(lambda l: [x.strip() for x in l])

