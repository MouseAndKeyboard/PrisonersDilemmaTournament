#!/usr/bin/env python3


import numpy as np

C = 1
D = 0

UNSURE = 0
ENEMY = 1
POSSIBLE_MINION = 2
DEFS_MINION = 3

def strategy(history, memory):
    god_protocol = [C, C, C, D, C]
    minion_protocol = [D, D, C, D, C]
    game_len = history.shape[1]

    opponent_history = history[1]
    my_history = history[0]

    if memory == DEFS_MINION:
        return C, DEFS_MINION

    if memory == POSSIBLE_MINION:
        if game_len < 5:
            choice = minion_protocol[game_len]
            if game_len != 0:
                matches_minion = minion_protocol[game_len - 1] == opponent_history[game_len - 1]

                if matches_minion:
                    memory = POSSIBLE_MINION
                    return minion_protocol[game_len], POSSIBLE_MINION
                memory = ENEMY
                return D, ENEMY
        else:
            return C, DEFS_MINION


    
    if memory == ENEMY:
        return D, ENEMY

    choice = C

    if game_len < 5:
        choice = minion_protocol[game_len]
        if game_len != 0:
            found_enemy = god_protocol[game_len - 1] != opponent_history[game_len - 1]
            matches_minion = minion_protocol[game_len - 1] == opponent_history[game_len - 1]

            if found_enemy:
                if matches_minion:
                    memory = POSSIBLE_MINION
                    return minion_protocol[game_len], POSSIBLE_MINION
                memory = ENEMY
                return D, ENEMY


    elif game_len == 13:
        choice = D
    elif game_len == 14:
        found_enemy = opponent_history[game_len - 1] != C
        if found_enemy:
            memory = ENEMY
            return D, memory
        else:
            choice = C
    elif game_len == 45:
        choice = D
    elif game_len == 46:
        found_enemy = opponent_history[game_len - 1] != C
        if found_enemy:
            memory = ENEMY
            return D, memory
        else:
            choice = C
    elif game_len > 6:
        if opponent_history[game_len - 1] != D:
            memory = ENEMY
            return D, memory
    else:
        # if opponent_history[game_len - 1] == C:
        #     memory = ENEMY
        #     return D, memory
        choice = C

    return choice, memory
