"""Let's calculate the probability of getting from $START to $TARGET, as opposed to busting out,
when using the martingale betting strategy, by doing empirical monte carlo simulations"""

START = 179.0
TARGET = 255
TRIALS = 1000
import random

def run_n_trials(n, _BET_SIZE):
    success = 0
    EV = 0
    for trial in range(n):
        usd = START
        bet_size = _BET_SIZE
        while usd > 0:
            #bet = min(usd, bet_size) #this is martingale strategy.
            bet = min(usd, TARGET-usd) #this is BOLD strategy. it's better but i didn't discover it until later
            #if usd == 103: #this may be one of infinitely many optimal strategies a la http://math.bme.hu/~nandori/Virtual_lab/stat/games/Optimal.pdf
            #    bet = 25
            usd -= bet
            if random.random() > 0.52:
                usd += bet*2
            else:
                bet_size *= 2
            if usd >= TARGET:
                success += 1
                EV += usd + 60#120
                break
        if usd <= 0:
            EV += - 40#40 -40
    #return EV/n
    return success/n

#for _BET_SIZE in (1, 2, 5, 10, 25, 50, 70, 80, 90, 100, 110, 120):
for _BET_SIZE in [80]:
    runs = [run_n_trials(TRIALS, _BET_SIZE) for i in range(100)]
    mean = sum(runs)/len(runs)
    print(_BET_SIZE, mean)

#motivation: bet with roommates that I could increase my bankroll from 176 to 255 playing online roulette.
# 2x $40:$60 odds with me having underdog odds.
#probability is around .6
#in the win case: I win $70 from roulette, $60 from each roommate
#win case: .6 * (70+60+60)
#in the lose case: I lose my $180, plus dole out $40 to each roommate
#lose case: .4*(-180 - 40 -40)
#EV: .6 * (70 + 60 + 60) + .4*(-180-40-40) = 10 (+ indulgence)
#conclusion: positive expected value.
