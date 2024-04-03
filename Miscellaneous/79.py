79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Solution:

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        t=set()
        def func(i,j,k):
            if k==len(word):
                return True
            if i<0 or j<0 or i>=m or j>=n or (i,j) in t or board[i][j]!=word[k]:
                return False
            t.add((i,j))
            ans= func(i+1,j,k+1) or func(i,j+1,k+1) or func(i-1,j,k+1) or func(i,j-1,k+1)
            t.remove((i,j))
            return ans

        m=len(board)
        n=len(board[0])
        l=len(word)
        for i in range(m):
            for j in range(n):
                if func(i,j,0):
                    return True
        return False
