This is a game of connect 4, following all of the rules of the real game.
To play, open in Idle, run the module, and type in connect4().
Depending on what setting you have put in (which I'll explain later), you will
either be prompted with a column in which to put your first token, or the
computer will go first. Continue playing, and may the best player win!!

Options:

PvP: To do this, uncomment the lines
#playerX = 'human'and #playerO = 'human'

PvAI: To do this, make sure the lines playerX = 'human' and 
playerO = Player('O', 'RANDOM', 4) are both uncommented. You can switch these if you want
the computer to go first.

AIvAI: To do this, make sure the lines playerO = Player('O', 'RANDOM', 4) and 
playerO = Player('O', 'RANDOM', 4) are both uncommented.

The third parameter in the Player class represents how far ahead into the game the AI
looks (how smart the computer is).