322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Solution:

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        t=[[0 for i in range(amount+1) ]for j in range(n+1)]
        
        for i in range(n+1):
            t[i][0]=0
        for j in range(amount+1):
            t[0][j]=100005
        for j in range(1,amount+1):
            if j%coins[0]==0:
                t[1][j]=j//coins[0]
            else:
                t[1][j]=100005
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i][j-coins[i-1]]+1,t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        return t[n][amount] if t[n][amount] != 100005 else -1
        
