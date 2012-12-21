class Elements:
    EMPTY = '.'
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

class Board:
    def __init__(self, player = Elements.EMPTY, positions = []):
        self.data = [ Elements.EMPTY for i in range(0,9) ]
        self.moveSet( player, positions )

    def copy(self):
        b = Board()
        b.data = self.data[:]
        return b

    def getHash(self):
        ret = ''.join(self.data)
        return ret + '\n'

    def getBoard(self):
        ret = '\n'.join([''.join(self.data[0:3]),''.join(self.data[3:6]),''.join(self.data[6:9])])
        return ret

    def getPlayerHash(self, player, token):
        r = []
        for i in self.data:
            if ( i == player ):
                r.append(token)
            else:
                r.append(Elements.EMPTY)
        return ''.join(r)

    def extractPlayerPositions(self, player, positions):
        for i in positions:
            if self.data[i] != player:
                return False

        return True

    def move(self, player, row, col):
        self.data[3*row+col] = player

    def move(self, player, position):
        self.data[position] = player

    def moveSet(self, player, positions):
        for i in positions:
            self.data[ i ] = player

    def evaluate(self, player):
        for pos in victory_positions:
            if self.extractPlayerPositions( player, pos ):
                return True

        return False

    def check_no_moves(self):
        if len(self.empty_spaces()) == 0:
            return True
        return False

    def empty_spaces(self):
        return [i for i,j in enumerate(self.getHash()) if j == Elements.EMPTY]
    

victory_positions = [ [0,1,2],[3,4,5],[6,7,8],
                      [0,3,6],[1,4,7],[2,5,8],
                      [0,4,8],[2,4,6] ]

victory_hash = {}
for pos in victory_positions:
    b = Board( Elements.PLAYER_1, pos )
    victory_hash[ b.getPlayerHash(Elements.PLAYER_1,'-') ] = 1
