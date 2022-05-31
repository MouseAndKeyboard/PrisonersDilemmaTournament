#!/usr/bin/env python3

import numpy as np

C = 1
D = 0

UNSURE = 0
ENEMY = 1

def default_good_strat(history, memory):
    choice = 1
    if history.shape[1] >= 2 and history[1,-1] == 0 and history[1,-2] == 0: # We check the TWO most recent turns to see if BOTH were defections, and only then do we defect too.
        choice = 0
    return choice, memory

def strategy(history, memory):
    god_protocol = [C, C, C, D, C]
    minion_protocol = [D, D, C, D, C]
    game_len = history.shape[1]

    opponent_history = history[1]
    my_history = history[0]

    if (memory == ENEMY):
        return default_good_strat(history, memory)



    if game_len < 5:
        choice = god_protocol[game_len]
        if game_len != 0:
            found_enemy = False
            found_enemy = minion_protocol[game_len - 1] != opponent_history[game_len - 1]
            if found_enemy:
                memory = ENEMY
                return default_good_strat(history, memory)
    elif game_len == 13:
        choice = C
    elif game_len == 14:
        found_enemy = opponent_history[game_len - 1] != D
        if found_enemy:
            memory = ENEMY
            return default_good_strat(history, memory)
        else:
            choice = D
    elif game_len == 45:
        choice = C
    elif game_len == 46:
        found_enemy = opponent_history[game_len - 1] != D
        if found_enemy:
            memory = ENEMY
            return default_good_strat(history, memory)
        else:
            choice = D
    elif game_len > 6:
        if opponent_history[game_len - 1] != C:
            memory = ENEMY
            return default_good_strat(history, memory)
        choice = D
    else:
        # if opponent_history[game_len - 1] == D:
        #     memory = ENEMY
        #     return default_good_strat(history, memory)
        choice = D
    return choice, memory
