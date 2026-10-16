# find winner of tiv tac toe game
#  Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). 
# In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[' '] * 3 for k in range(3)]

        for i in range(len(moves)):
            r, c = moves[i]
            if i % 2 == 0:
                grid[r][c] = 'X'
            else:
                grid[r][c] = 'O'

        lines = []
        for i in range(3):
            lines.append([grid[i][0], grid[i][1], grid[i][2]])  
            lines.append([grid[0][i], grid[1][i], grid[2][i]])  
        lines.append([grid[0][0], grid[1][1], grid[2][2]])      
        lines.append([grid[0][2], grid[1][1], grid[2][0]])      

        for line in lines:
            if line == ['X', 'X', 'X']:
                return "A"
            if line == ['O', 'O', 'O']:
                return "B"

        if len(moves) == 9:
            return "Draw"
        return "Pending"