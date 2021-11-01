import argparse
import random
import json
import sys
from collections import defaultdict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    #get the arguments
    curr_args = parser.parse_args()
    cellmates_lastmove = curr_args.last_opponent_move

    if cellmates_lastmove == "zero":
        my_move = "confess"
        cellmates_years = 0
        my_years = 0
    else:
        textlist = []
        #read from the text file
        with open('moveFile.txt', "r") as infile:
            text_list=[w for line in infile for w in line.split(' ')]
        print(textlist)
        my_move = textlist[1]
        cellmates_years = textlist[2]
        my_years = textlist[3]

    if cellmates_lastmove == "confess":
        my_move = "silent"

    move_list = [cellmates_lastmove, my_move, cellmates_years, my_years]
    move_file = open('moveFile.txt', 'w')
    for mv in move_list:
        move_file.write(' %s' % mv)
    move_file.write('\n')
    move_file.close()


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

   # with open('lazyMoves.json', 'r') as infile:
   #     moves_data = json.load(infile)

    #print(args.last_opponent_move)
    #print('confess')
    # print(my_lazy_move)
    #my_lazy_move = args.last_opponent_move
    #print( random.choice(['confess', 'silent']) )
    print(my_move)