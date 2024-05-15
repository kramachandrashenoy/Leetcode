1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Solution:

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        maxi=0

        def board():
            return [[False for _ in range(cols)]for _ in range(rows)]
        def func(i,j,total,board):
            if grid[i][j]==0 or board[i][j]==True:
                return total
            board[i][j]=True
            total+=grid[i][j]

            local_maxi=0
            if i>0:
                local_maxi=max(local_maxi,func(i-1,j,total,board))
            if j>0:
                local_maxi=max(local_maxi,func(i,j-1,total,board))
            if i<rows-1:
                local_maxi=max(local_maxi,func(i+1,j,total,board))
            if j<cols-1:
                local_maxi=max(local_maxi,func(i,j+1,total,board))
            
            board[i][j]=False
            return local_maxi
        for i in range(rows):
            for j in range(cols):
                maxi=max(maxi,func(i,j,0,board()))
        return maxi

        
