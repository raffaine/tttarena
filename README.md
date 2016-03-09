Bot Arena for Tic Tac Toe

The main goal is to have a place to understand simple AI agent design.
All agents, known as Bots, must use stdin and stdout to percept and act.

PROTOCOL
First message is your player, i.e 'X' or 'O'

X will allways start the game

Each player receive (in turns) the game state represented by '.' when is empty

Ex: ...X..O..

When some player wins, all bots receive the string 'win', 'draw' or 'loose'


You only need a Python 2.7

runtime.py :: The Bot Arena ... it's still predef the fighting bots (TODO)

tttboard.py :: A class that represents the game state and evaluation

loxas.py :: My Bot implementation using Min-Max

rand.py :: A random bot
