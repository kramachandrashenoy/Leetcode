# DIffernece between 0-1 knapsack and unbounded knapsack is that in unbounded knapsack if the item is considered once it might be taken into consideration again which is not the case in 0-1 knapsack.

wt=[10,20,30]
val=[60,100,120]
W = 50
n = 3

t=[[0 for i in range(W+1)]for j in range(n+1)]

for i in range(n+1):
    for j in range(W+1):
        if n==0 or W==0:
            t[i][j]=0
        if wt[i-1]<=j:
            t[i][j]=max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j]) # The difference lies here if the weight is subtracted then the same element is considered again.
        elif wt[i-1]>j:
            t[i][j]=t[i-1][j]
print("The maximum profit using DP is "+str(t[n][W]))
