#!/usr/bin/env python

import random
import sys

empty_char ='.' 

def empty_squares(board):
    '''Return the empty squares in a board'''
    return [i for i,j in enumerate(board) if j == empty_char]

def random_strategy(player, board):
    '''A not so clueless strategy'''
    esquares = empty_squares(board)
    return random.choice(esquares) if esquares else 0

def client(strategy):
    '''A client to run a strategy of tic-tac-toe'''
    player = sys.stdin.readline()
    while True:
        msg = sys.stdin.readline()
        if msg[:-1] in ['win','lose','draw']:
            return msg
        else:
            sys.stdout.write(str(strategy(player, msg))+'\n')
            sys.stdout.flush()

client(random_strategy)
