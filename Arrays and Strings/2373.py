2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Solution:

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new_matrix=[[0 for j in range(len(grid[0])-2)]for i in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                maxi=float('-inf')
                for  k in range(3):
                    for l in range(3):
                        if maxi<grid[i+k][j+l]:
                            maxi=grid[i+k][j+l]
                new_matrix[i][j]=maxi
        return new_matrix



        
