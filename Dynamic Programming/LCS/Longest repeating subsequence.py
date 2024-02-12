The major difference is that we consider the duplicate of the string and then we find the LCS with the condition i!=j so that all the other repeating alphabets can be considered.
class Solution:
	def LongestRepeatingSubsequence(self, str):
		return longestRepeatingSubsequence(str, str, len(str), len(str))

def longestRepeatingSubsequence(X, Y, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if(X[i-1] == Y[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]
