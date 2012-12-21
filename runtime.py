import sys
from subprocess import Popen, PIPE

from tttboard import *

def main(argv):
    b = Board()
    
    bots = [(Popen('rand.py', bufsize=1, stdout=PIPE, stdin=PIPE, shell=True, universal_newlines=True), Elements.PLAYER_1),
            (Popen('loxas.py', bufsize=1, stdout=PIPE, stdin=PIPE, shell=True, universal_newlines=True), Elements.PLAYER_2)]

    turn = 0

    #initialize bots
    for bot in bots:
        bot[0].stdin.write(bot[1]+'\n')
        bot[0].stdin.flush()

    #game loop
    while True:
        bots[turn][0].stdin.write(b.getHash())
        bots[turn][0].stdin.flush()
        play = bots[turn][0].stdout.readline()
        print 'Player ' + bots[turn][1] + ' plays ' + play    
        b.move(bots[turn][1], int(play[0:-1]))
        s = b.getBoard()
        print s
        
        if b.evaluate(bots[turn][1]):
            break
        elif b.check_no_moves():
            print 'Draw'
            for bot in bots:
                bot[0].stdin.write('draw\n')
                bot[0].stdin.flush()
            return
        
        turn = (turn + 1) % 2

    #end of game
    print  'Player ' + bots[turn][1] + ' wins'

    for i in range(0,1):
        bots[i][0].stdin.write( 'win\n' if i == turn else 'lose\n' )
        bots[i][0].stdin.flush()
    
        
if __name__ == "__main__":
  #  if( len(sys.argv) < 3 ):
   #     print "Too few arguments"
    #    exit(0)
    
    main(sys.argv[1:])
