import sys
import random

from tttboard import *

player = Elements.PLAYER_1
opponent = Elements.PLAYER_2

class node:
    def __init__(self, minmaxval = True, board = Board()):
        self.children = []
        self.value = 0
        self.board = board
        self.max = minmaxval

    def __eq__(self, other):
        return self.board.getHash() == other

    def __cmp__(self, other):
        return cmp(self.value, other.value)

    def generate(self):
        flag = False
        (who,sig) = (player,1) if self.max else (opponent,-1)
	
        for i in self.board.empty_spaces():            
            n = node(not self.max, self.board.copy())
            n.board.move(who, i)
            n.value = n.evaluate(who)
            flag = flag or (n.value == 1)
            n.value *= sig
            
            self.children.append(n)
			
        if flag:
            filter(lambda x: x.value/sig == 1, self.children)
            for child in self.children:
                self.value += child.value            
        else:
            for child in self.children:
                child.generate()

            if len(self.children) == 0:
                self.value = 0
            else:
                self.value = max(self.children).value if self.max else min(self.children).value

        
    def evaluate(self, who):
        return 1 if self.board.evaluate(who) else 0

def client(strategy):
    '''A client to run a strategy of tic-tac-toe'''
    global player
    global opponent
    
    start = True
    player = sys.stdin.readline()[:-1]
    
    if player == opponent:
        opponent = Elements.PLAYER_1
        start = False

    arv = node(start)
    arv.generate()
    #print 'ready'
    
    while True:
        msg = sys.stdin.readline()
        if msg[:-1] in ['win','lose','draw']:
            return
        else:
            if start:
                start = False
            else:
                arv = arv.children[ arv.children.index(msg) ]

            b = arv.board
            arv = max(arv.children)
            
            diff = [ i for i,(left,right) in enumerate(zip(b.getHash(),arv.board.getHash())) if left != right]
            sys.stdout.write(str(diff[0])+'\n')
            sys.stdout.flush()

if __name__ == "__main__":
    client(1)
