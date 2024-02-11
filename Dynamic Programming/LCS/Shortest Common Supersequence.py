# Prints the shortest common supersequence
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m=len(str1)
        n=len(str2)
        t=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        i=m
        j=n
        ans=str()
        while(i>0 and j>0):
            if str1[i-1]==str2[j-1]:
                ans+=str1[i-1]
                i-=1
                j-=1
            else:
                if t[i-1][j]>t[i][j-1]:
                    ans+=str1[i-1]
                    i-=1
                else:
                    ans+=str2[j-1]
                    j-=1
        # If any of the strings is empty we need the below conditions
        while i>0:
            ans+=str1[i-1]
            i-=1
        while j>0:
            ans+=str2[j-1]
            j-=1
        return ans[::-1]
# To print the length of the shortest common supersequence we add the length of the two string and subtract the LCS.
