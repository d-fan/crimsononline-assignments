import random

def lookaway(trials):
    win_count = 0
    for trial in xrange(0,trials):
        lose = [False] * 3
        for rnd in range(0,5):
            for player in range(0,3):
                # If any player looks forward, that player loses
                if(random.randrange(5) == 0):
                    lose[player] = True
        # If all players have lost after 5 rounds, Luigi wins
        if (lose == [True]*3):
            win_count += 1
    return win_count/float(trials)

#print lookaway(100)
