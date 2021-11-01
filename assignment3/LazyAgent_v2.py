import argparse
import random
import json
import sys
from collections import defaultdict
"""
Lazy agent, yes really lazy. I tried but could not get the json working, 
not sure how not to assign a new list in each iteration. So, I gave up
and use this simple code with dummy logic
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    #get the arguments
    curr_args = parser.parse_args()
    cellmates_lastmove = curr_args.last_opponent_move

    my_move = 'confess'
    if cellmates_lastmove == "zero":
        my_move = "confess"
        cellmates_years = 0
        my_years = 0
        my_score = 0

    if cellmates_lastmove == "confess":
        my_move = "silent"
    """
    with open('score_file.txt') as outfile:
        my_years = outfile.readline()
    print(my_years)
    """
    print(my_move)
    """
    if cellmates_lastmove == "zero": curr_iter = 1
    else: curr_iter = 0 + 1
    moves['curr_iter'] = { 'cellmatesMove': cellmates_lastmove, 'years': my_years}

    cellmates_movelist = []
    cellmates_movelist.append(cellmates_lastmove)
    move_keys = {"lastMove", "myPrevMove", "myYrs", "cellMatesYrs"}
    move_vals = {cellmates_lastmove, my_move, my_years, cellmates_years}
    #movelist_dict(list(enumerate(move_vals)))
    movelist_dict = dict(zip(move_keys, move_vals))
    
    with open('lazyMoves.json', 'w') as outfile:
        json.dump(moves, outfile, indent=2)
    """
