class Solution:
	def minOperations(self, s1, s2):
	    lcs = LCSDP(s1, s2, len(s1), len(s2))
	    numOfDel = len(s1) - lcs
	    numOfIns = len(s2) - lcs
	    return numOfDel + numOfIns


def LCSDP(X, Y, n, m):
    dp = [[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(X[i-1] == Y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[n][m]
