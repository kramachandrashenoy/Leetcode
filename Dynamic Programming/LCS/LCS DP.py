class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m=len(text1)
        n=len(text2)
        t=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    t[i][j]=0
                else:
                    if text1[i-1]==text2[j-1]:
                        t[i][j]=1+t[i-1][j-1]
                    else:
                        t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[m][n]
